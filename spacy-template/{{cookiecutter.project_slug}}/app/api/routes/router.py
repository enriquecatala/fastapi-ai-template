"""
 Contact me:
   e-mail:   enrique@enriquecatala.com 
   Linkedin: https://www.linkedin.com/in/enriquecatala/
   Web:      https://enriquecatala.com
   Twitter:  https://twitter.com/enriquecatala
   Support:  https://github.com/sponsors/enriquecatala
   Youtube:  https://www.youtube.com/enriquecatala
   
"""

from fastapi import APIRouter

from app.api.routes import heartbeat, prediction

api_router = APIRouter()
api_router.include_router(heartbeat.router, tags=["health"], prefix="/health")
api_router.include_router(prediction.router, tags=["prediction"], prefix="/model")
