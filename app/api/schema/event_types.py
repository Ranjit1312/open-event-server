from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.event_type import EventType

# using the SQLAlchemyAutoSchema:


class AuthorSchema(SQLAlchemyAutoSchema):


    class Meta:
        model = EventType
        include_relationships = True
        include_fk = True
        load_instance = True  # Optional: deserialize to model instances