from modules.decorators import view, query, event_handler, memoize_query
#from an_evt.models import StudentBookAccesses
from django.contrib.auth.models import User
from courseware.models import StudentModule
import json
from django.conf import settings
import logging
from django.utils import timezone
import datetime
from modules import common

log=logging.getLogger(__name__)
import re

from mitxmako.shortcuts import render_to_response, render_to_string

@query('course', 'total_user_count')
def users_in_course_count_query(fs, db, course,params):
    return StudentModule.objects.filter(course_id=course).values('student').distinct().count()

@query('course', 'modules_accessed_count')
def modules_accessed_in_course_count_query(fs, db, course, params):
    return StudentModule.objects.filter(course_id=course).count()

@query('course', 'problems_tried_count')
def problems_tried_in_course_count_query(fs, db, course, params):
    return StudentModule.objects.filter(course_id=course,module_type="problem").count()

@query('course', 'video_watch_count')
def videos_watched_in_course_count_query(fs, db, course, params):
    return StudentModule.objects.filter(course_id=course,module_type="video").count()

@view('course', 'total_user_count')
def users_in_course_count_view(fs, db, course, params):
    return "The system has "+str(users_in_course_count_query(fs,db,course,params)) + " users total"

@view('course', 'modules_accessed_count')
def modules_accessed_in_course_count_view(fs, db, course, params):
    return str(modules_accessed_in_course_count_query(fs,db,course,params)) + " modules accessed in the course."

@view('course', 'problems_tried_count')
def problems_tried_in_course_count_view(fs, db, course, params):
    return str(problems_tried_in_course_count_query(fs,db,course,params)) + " problems tried in the course."

@view('course', 'video_watch_count')
def videos_watched_in_course_count_view(fs, db, course, params):
    return str(videos_watched_in_course_count_query(fs,db,course,params)) + "videos watched in the course."

@query('global', 'users_per_course_count')
def users_per_course_count_query():
    query_string = "SELECT course_id, COUNT(DISTINCT user_id) AS count FROM student_courseenrollment GROUP BY course_id"
    return common.query_results(query_string)

@view('global', 'users_per_course')
def users_per_course_count_view():
    query_data = users_per_course_count_query()
    return common.render_query_as_table(query_data)

@query('global', 'new_students')
@memoize_query(cache_time=15*60)
def new_course_enrollment_query(fs, db, params):
    r = common.query_results("SELECT course_id,COUNT(DISTINCT student_id) FROM `courseware_studentmodule` WHERE DATE(created) >= DATE(DATE_ADD(NOW(), INTERVAL -7 DAY)) GROUP BY course_id;")
    return r

@view('global', 'new_students')
def new_course_enrollment_view(fs, db, params):
    r = new_course_enrollment_query(fs,db,params)
    return common.render_query_as_table(r)

