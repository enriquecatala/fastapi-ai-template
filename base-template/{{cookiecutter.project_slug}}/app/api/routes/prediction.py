"""
 Contact me:
   e-mail:   enrique@enriquecatala.com 
   Linkedin: https://www.linkedin.com/in/enriquecatala/
   Web:      https://enriquecatala.com
   Twitter:  https://twitter.com/enriquecatala
   Support:  https://github.com/sponsors/enriquecatala
   Youtube:  https://www.youtube.com/enriquecatala
   
"""

from fastapi import APIRouter, Depends
from fastapi.requests import Request

from app.core import security
from app.models.payload import Payload
from app.models.prediction import Result
from app.services.models import AIModel

router = APIRouter()


@router.post("/test", response_model=Result, name="test")
def post_predict(
    request: Request,
    authenticated: bool = Depends(security.validate_request),
    block_data: Payload = None
) -> Result:

    model: AIModel = request.app.state.model
    prediction: Result = model.test(block_data)

    return prediction
