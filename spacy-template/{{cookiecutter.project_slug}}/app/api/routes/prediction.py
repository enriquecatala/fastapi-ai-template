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
from app.models.payload import AIPredictionPayload
from app.models.prediction import AIPredictionResult
from app.services.models import AIModel

router = APIRouter()


@router.post("/list_of_orgs", response_model=AIPredictionResult, name="list_of_orgs")
def post_predict(
    request: Request,
    authenticated: bool = Depends(security.validate_request),
    block_data: AIPredictionPayload = None
) -> AIPredictionResult:

    model: AIModel = request.app.state.model
    prediction: AIPredictionResult = model.get_list_of_orgs(block_data)

    return prediction
