"""
 Contact me:
   e-mail:   enrique@enriquecatala.com 
   Linkedin: https://www.linkedin.com/in/enriquecatala/
   Web:      https://enriquecatala.com
   Twitter:  https://twitter.com/enriquecatala
   Support:  https://github.com/sponsors/enriquecatala
   Youtube:  https://www.youtube.com/enriquecatala
   
"""

from typing import List
from pydantic import BaseModel


## This is the Payload (for the prediction)
class Payload(BaseModel):
    texts: List[str]
    


def payload_to_list(hpp: Payload) -> List:
    return [
        hpp.texts        
        ]
