from marshmallow import Schema, EXCLUDE, fields, post_load
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow_enum import EnumField
from core.models.teachers import Teacher
from core.models.assignments import Assignment, GradeEnum
from core.libs.helpers import GeneralObject

class TeacherSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Teacher
        unknown = EXCLUDE

    id = auto_field()
    user_id = auto_field()
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)

    @post_load
    def initiate_class(self, data_dict, many, partial):
        return Teacher(**data_dict)
