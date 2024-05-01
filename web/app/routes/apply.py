from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from app.schemas.visitors import Visitors
from app.services.visitors import VisitorsService
from app.services.employee import EmployeeService

from app.services.location import LocationService

from fastapi import HTTPException

apply_router = APIRouter()

templates = Jinja2Templates(directory='views/templates')


@apply_router.get('/', response_class=HTMLResponse)
def apply(req: Request):
    emp_list = EmployeeService.get_all_employees()
    location_list = LocationService.get_all_location()
    return templates.TemplateResponse('apply/apply.html', {'request': req, 'emp_list': emp_list, 'location_list': location_list})



@apply_router.post('/applyok')
def applyok(vmdto: Visitors):
    print(vmdto)
    result = VisitorsService.insert_visitor(vmdto)
    return result.rowcount


@apply_router.get('/applyok', response_class=HTMLResponse)
def applycheck(req: Request):
    return templates.TemplateResponse('apply/applyok.html', {'request': req})


