"""
 Contact me:
   e-mail:   enrique@enriquecatala.com 
   Linkedin: https://www.linkedin.com/in/enriquecatala/
   Web:      https://enriquecatala.com
   Twitter:  https://twitter.com/enriquecatala
   Support:  https://github.com/sponsors/enriquecatala
   Youtube:  https://www.youtube.com/enriquecatala
   
"""
from typing import Dict,List
from pydantic import BaseModel


class ClassificationResult(BaseModel):
    """
      A class to represent a prediction result.

      Attributes
      ----------      
      orgs : List[str]
          List of organizations (Tesla, MSFT,...)      
      orgs_cleaned : List[str]
          List of organizations (Tesla, MSFT,...) after cleaning

      Methods
      -------
      None
    """  
    orgs: List[str]
    orgs_cleaned: List[str]
class AIPredictionResult(BaseModel):
    """
    A class to represent a prediction result.

    Attributes
    ----------
    result
      id_paragraph: int
          Id of the paragraph we are getting the sentiment
      Dict[id_paragraph, ClassificationResult]

      This is the output expected
            {
                "result": {
                    "0": {
                        "orgs": [
                            "Tesla",
                            "Tesla2",
                            "Coinbase",
                            "$coinbase..."
                        ],
                        "orgs_cleaned": [
                            "Tesla",
                            "Coinbase"
                        ]
                    },
                    "1": {
                        "orgs": [],
                        "orgs_cleaned": []
                    },
                    ...
                }
            }

    """
    result: Dict[int,ClassificationResult]
    
