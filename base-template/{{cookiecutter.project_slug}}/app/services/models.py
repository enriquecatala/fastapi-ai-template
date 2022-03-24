"""
 Contact me:
   e-mail:   enrique@enriquecatala.com 
   Linkedin: https://www.linkedin.com/in/enriquecatala/
   Web:      https://enriquecatala.com
   Twitter:  https://twitter.com/enriquecatala
   Support:  https://github.com/sponsors/enriquecatala
   Youtube:  https://www.youtube.com/enriquecatala
   
"""
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
from app.models.payload import (Payload,payload_to_list)
from app.models.prediction import Result
from app.core import config

#####
# Imports for your model
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
        
        logger.info("*****MODEL LOADDED*****")

    def _pre_process(self, payload: Payload) -> Dict[int,str]:
        """
        Returns a dictionary with the id_paragraph,SpacyDocs

        Args:
            payload (Payload): texts
        Returns:
            dict[int,str]: <id_paragraph, str>
        """
        logger.debug("Pre-processing payload.")

        # for all comments in the list i create a single list containing all the phrases
        retorno={}        
        # for all values in payload.texts create a dict starting in 1
        for idx,text in enumerate(payload.texts):
            retorno[idx+1]=text            
        
        return retorno

    def _post_process(self, data: Dict[int,str]) -> Result:
        """
        It returns the AIPredictionResult

        Args:
            list_of_orgs(dict): Is a Dict[id_paragraph,ClassificationResult] object
        """
        logger.debug("Post-processing prediction.")
        
        hpp = Result(result=data)
        return hpp
   
 
    def test(self, payload: Payload):
        """
        Main method. 

        Args:
            payload (Payload): Object with the paragraphs to analize

        Returns:
            Result: Result object
           
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
