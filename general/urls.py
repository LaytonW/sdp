from django.conf.urls import url
from .views import participant,instructor,authenticate,administrator

participantURL = r'^Participant/(?P<participantID>[0-9]+)'
instructorURL = r'^Instructor/(?P<instructorID>[0-9]+)'
courseURL = instructorURL+r'/(?P<courseID>[0-9]+)'
moduleURL = courseURL + r'/(?P<moduleIndex>[0-9]+)'
administratorURL=r'^Administrator/(?P<administratorID>[0-9]+)'

urlpatterns = [
    url(participantURL+r'$',participant.ParticipantIndex,name="ParticipantIndex"),
    url(participantURL+r'/showCourseList$',participant.showCourseList,name="showCourseList"),
    url(participantURL+r'/showCourse$',participant.showCourse,name="showCourse"),
    url(participantURL+r'/enroll$',participant.enroll,name="enroll"),
    url(participantURL+r'/((?P<courseID>[0-9]+))$',participant.viewCourse,name="viewCourse"),
    url(instructorURL+r'$',instructor.InstructorIndex,name="InstructorIndex"),
    url(instructorURL+r'/newCourse$',instructor.newCourse,name="newCourse"),
    url(courseURL+r'$',instructor.coursePage,name="coursePage"),
    url(courseURL+r'/changeModuleOrder$',instructor.changeModuleOrder,name="changeModuleOrder"),
    url(courseURL+r'/newModule$',instructor.newModule,name="newModule"),
    url(courseURL+r'/editCourse$',instructor.editCourse,name="editCourse"),
    url(moduleURL+r'$',instructor.modulePage,name="modulePage"),
    url(moduleURL+r'/changeComponentOrder$',instructor.changeComponentOrder,name="changeComponentOrder"),
    url(moduleURL+r'/newComponent$',instructor.newComponent,name="newComponent"),
    url(administratorURL+r'$',administrator.AdministratorIndex,name="AdministratorIndex"),
    url(r'login/$',authenticate.myLogin,name="myLogin"),
    url(r'^$',authenticate.myLogin,name="homeLogin"),
    url(r'logout/$',authenticate.myLogout,name="myLogout"),
    url(r'register/$',authenticate.register,name="register"),
]
