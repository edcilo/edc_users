from sqlalchemy import or_
from ms.models import App
from .repository import Repository


class AppRepository(Repository):
    def get_model(self):
        return App

    def all(self,
            search=None,
            order_column='created_at',
            order='desc',
            paginate=False,
            page=1,
            per_page=15):
        column = getattr(self._model, order_column)
        order_by = getattr(column, order)
        q = self._model.query
        if search is not None:
            q = q.filter(or_(self._model.name.like(f'%{search}%'),
                             self._model.description.like(f'%{search}%')))
        q = q.order_by(order_by())
        return q.paginate(page, per_page=per_page) if paginate else q.all()
