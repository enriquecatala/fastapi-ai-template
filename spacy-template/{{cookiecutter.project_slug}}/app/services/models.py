"""
 Contact me:
   e-mail:   enrique@enriquecatala.com 
   Linkedin: https://www.linkedin.com/in/enriquecatala/
   Web:      https://enriquecatala.com
   Twitter:  https://twitter.com/enriquecatala
   Support:  https://github.com/sponsors/enriquecatala
   Youtube:  https://www.youtube.com/enriquecatala
   
"""
import torch
from typing import List,Dict
import numpy as np
import traceback
from loguru import logger
import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler

from fastapi.responses import JSONResponse
from fastapi import status
from fastapi.encoders import jsonable_encoder

from app.core.messages import NO_VALID_PAYLOAD
from app.models.payload import (AIPredictionPayload,
                                             payload_to_list)
from app.models.prediction import AIPredictionResult, ClassificationResult
from app.core import config

#####
# Imports for your model
import spacy
import re
#####

class AIModel(object):

    def __init__(self, path):
        #AppInsights
        self.app_insights = logging.getLogger(config.APP_NAME)
        self.app_insights.addHandler(AzureLogHandler(
                connection_string=f"InstrumentationKey={config.APPLICATION_INSIGHTS_KEY}")
        )
        self.app_insights.setLevel(logging.INFO)
        #

        self.path = path
        self._load_local_model()        

    def _load_local_model(self):
        # TODO: INCLUDE YOUR MODEL LOADING
        if torch.cuda.is_available():            
            
            #spacy.require_gpu()  # this will fail if gpu is not present
            gpu = spacy.prefer_gpu()            
            logger.info("CUDA HARDWARE DETECTED!. Using device {}".format(gpu))
        else: 
            logger.info("cuda hardware not detected")

        #self.nlp = spacy.load('en_core_web_trf')    
        self.nlp = spacy.load(self.path)

        logger.info("*****MODEL LOADDED*****")

    def _pre_process(self, payload: AIPredictionPayload) -> dict:
        """
        Returns a dictionary with the id_paragraph,SpacyDocs

        Args:
            payload (AIPredictionPayload): texts
        Returns:
            dict[int,SpacyDoc]: <id_paragraph, SpacyDoc>
        """
        logger.debug("Pre-processing payload.")

        # for all comments in the list i create a single list containing all the phrases
        retorno={}        
        for i in range(len(payload.texts)):
            tmp_result = []
            #this returns a list of phrases
            tmp = self.nlp(payload.texts[i])
            tmp_result.append(tmp)


            #add to the retorno dictionary <i,phrases> only if list is not empty
            if len(tmp_result)>0:
                retorno[i]=tmp_result

        return retorno

    def _post_process(self, data: Dict[int,ClassificationResult]) -> AIPredictionResult:
        """
        It returns the AIPredictionResult

        Args:
            list_of_orgs(dict): Is a Dict[id_paragraph,ClassificationResult] object
        """
        logger.debug("Post-processing prediction.")
        
        hpp = AIPredictionResult(result=data)
        return hpp
   

    def _clean(self, list_of_orgs: List[str]) -> List[str]:    
        """
        Cleans up the list of phrases, removing unncesary characters and duplicates
        """
        retorno = [self.compiled_re_to_clean_words.sub('', i).lower() for i in list_of_orgs]
        retorno = list(set(retorno))
        return retorno
    
    def predict(self, payload: AIPredictionPayload):
        """
        Main method. 

        Args:
            payload (AIPredictionPayload): Object with the paragraphs to analize

        Returns:
            AIPredictionResult: Result object with the list of organizations and in which paragraph has been detected
           
        """
        if payload is None:
            raise ValueError(NO_VALID_PAYLOAD.format(payload))

        try:
            pre_processed = self._pre_process(payload)                     
          
            # now i´m getting the last value as a single unique value for all the classification
            post_processed_result = self._post_process(pre_processed)
            
        except Exception as e:            
            #logger.exception(traceback.print_exc())
            logger.exception(e)
            self.app_insights.exception(e)
            raise e
            
            
        return post_processed_result
