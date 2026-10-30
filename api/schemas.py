from pydantic import BaseModel, Field

class PredictionRequest(BaseModel):
    credito: Field(ge=0, description="Valor do credito")

class PredictionResponse(BaseModel):
    resposta: str = Field(description="Classificacao: baixo, medio, alto")