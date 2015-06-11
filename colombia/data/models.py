from sqlalchemy.ext.hybrid import hybrid_property

from atlas_core.sqlalchemy import BaseModel
from atlas_core.model_mixins import IDMixin

from ..core import db

from ..metadata.models import (Location, HSProduct)

class DepartmentProductYear(BaseModel, IDMixin):

    __tablename__ = "department_product_year"

    department_id = db.Column(db.Integer, db.ForeignKey(Location.id))
    product_id = db.Column(db.Integer, db.ForeignKey(HSProduct.id))
    year = db.Column(db.Integer)

    department = db.relationship(Location)
    product = db.relationship(HSProduct)

    import_value = db.Column(db.Integer)
    export_value = db.Column(db.Integer)
    export_rca = db.Column(db.Integer)
    density = db.Column(db.Float)
    cog = db.Column(db.Float)
    coi = db.Column(db.Float)

    @hybrid_property
    def distance(self):
        return 1.0 - self.density

    @distance.expression
    def distance(cls):
        return (1.0 - cls.density).label("distance")


class DepartmentYear(BaseModel, IDMixin):

    __tablename__ = "department_year"

    department_id = db.Column(db.Integer, db.ForeignKey(Location.id))
    year = db.Column(db.Integer)

    department = db.relationship(Location)

    eci = db.Column(db.Float)
    eci_rank = db.Column(db.Integer)
    diversity = db.Column(db.Float)


class ProductYear(BaseModel, IDMixin):

    __tablename__ = "product_year"

    product_id = db.Column(db.Integer, db.ForeignKey(HSProduct.id))
    year = db.Column(db.Integer)

    product = db.relationship(HSProduct)

    pci = db.Column(db.Float)
    pci_rank = db.Column(db.Integer)