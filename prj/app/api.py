from ninja import NinjaAPI, Schema
from app.models import Artwork, Person
from typing import List


api = NinjaAPI()


class ArtworkSchema(Schema):
    id: int | None = None
    name: str
    material: str
    creator: str | None = None


class ArtworkListingSchema(Schema):
    count: int
    results: List[ArtworkSchema]


class MessageSchema(Schema):
    message: str


@api.get("/artwork", response=ArtworkListingSchema)
def get_artworks(request):

    artworks = Artwork.objects.all()

    out = []

    for artwork in artworks:

        out.append({
            "id": artwork.id,
            "name": artwork.name,
            "material": artwork.material,
            "creator": artwork.creator.name if artwork.creator else None
        })

    return {
        "count": len(out),
        "results": out
    }


@api.get("/artwork/{artwork_id}", response={200: ArtworkSchema, 404: MessageSchema})
def get_artwork(request, artwork_id: int):

    try:

        artwork = Artwork.objects.get(id=artwork_id)

        return {
            "id": artwork.id,
            "name": artwork.name,
            "material": artwork.material,
            "creator": artwork.creator.name if artwork.creator else None
        }

    except Artwork.DoesNotExist:

        return 404, {
            "message": "Artwork not found"
        }


@api.post("/artwork", response={201: ArtworkSchema, 400: MessageSchema})
def create_artwork(request, data: ArtworkSchema):

    try:

        creator = None

        if data.creator:
            creator, _ = Person.objects.get_or_create(
                name=data.creator
            )

        artwork = Artwork.objects.create(
            name=data.name,
            material=data.material,
            creator=creator
        )

        return 201, {
            "id": artwork.id,
            "name": artwork.name,
            "material": artwork.material,
            "creator": artwork.creator.name if artwork.creator else None
        }

    except Exception as e:

        return 400, {
            "message": str(e)
        }


@api.put("/artwork/{artwork_id}", response={200: ArtworkSchema, 400: MessageSchema, 404: MessageSchema})
def update_artwork(request, artwork_id: int, data: ArtworkSchema):

    try:

        artwork = Artwork.objects.get(id=artwork_id)

        creator = None

        if data.creator:
            creator, _ = Person.objects.get_or_create(
                name=data.creator
            )

        artwork.name = data.name
        artwork.material = data.material
        artwork.creator = creator

        artwork.save()

        return {
            "id": artwork.id,
            "name": artwork.name,
            "material": artwork.material,
            "creator": artwork.creator.name if artwork.creator else None
        }

    except Artwork.DoesNotExist:

        return 404, {
            "message": "Artwork not found"
        }

    except Exception as e:

        return 400, {
            "message": str(e)
        }
