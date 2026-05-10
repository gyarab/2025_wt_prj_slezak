from ninja import NinjaAPI, Schema
from typing import List
from .models import Artwork

api = NinjaAPI()



class ArtworkSchema(Schema):
    id: int
    name: str
    material: str


@api.get("/artwork", response=List[ArtworkSchema])
def artworks(request):
    return Artwork.objects.all()



@api.get("/artwork/{artwork_id}", response=ArtworkSchema)
def artwork_detail(request, artwork_id: int):
    return Artwork.objects.get(id=artwork_id)