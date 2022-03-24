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

   
class Result(BaseModel):
    """
    A class to represent a result.

    Attributes
    ----------
    result
      dict[int,str]

    """
    result: Dict[int,str]
    
