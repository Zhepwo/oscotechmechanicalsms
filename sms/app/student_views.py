from django.shortcuts import render, redirect
from app.models import Student_Notification, Student, Student_Feedback, Student_Leave, Subject, Attendance, Attendance_Report, StudentResult, Course
from django.contrib import messages
from django.contrib.auth.decorators import login_required


    
@login_required(login_url='/')
def HOME(request):
    student_id = Student.objects.get(admin=request.user.id) 
    total_attendance = Attendance_Report.objects.filter(student_id=student_id).count()
    time_present = Attendance_Report.objects.filter(student_id=student_id, status=True).count()
    time_absent = Attendance_Report.objects.filter(student_id=student_id, status=False).count()

    course = Course.objects.get(id=student_id.course_id.id)
    subjects = Subject.objects.filter(course=course.id).count()

    subject_name = []
    data_present = []
    data_absent = []
    subject_data = Subject.objects.filter(course=student_id.course_id)
    
    for i in subject_data:
        attendance = Attendance.objects.filter(subject_id=i.id)
        attendance_present_count = Attendance_Report.objects.filter(attendance_id__in=attendance, status=True,student_id=student_id.id).count()
        attendance_absent_count = Attendance_Report.objects.filter(attendance_id__in=attendance, status=False,student_id=student_id.id).count()
        subject_name.append(i.name)
        data_present.append(attendance_present_count)
        data_absent.append(attendance_absent_count)
    
    context = {
        'total_attendance': total_attendance,
        'attendance_present_count': attendance_present_count,
        'attendance_absent_count': attendance_absent_count,
        'time_present': time_present,
        'time_absent': time_absent,
        'subjects': subjects,
        'subject_name':subject_name,
        'data_present':data_present,
        'data_absent': data_absent,
        
    }
    
    return render(request, 'student/home.html', context)





def STUDENT_NOTIFICATION(request):
    student = Student.objects.filter(admin=request.user.id)
    for i in student:
        student_id = i.id
        
        notification = Student_Notification.objects.filter(student_id=student_id)
        
        context = {
            'notification': notification
        }
    return render(request, 'student/notification.html', context)




def STUDENT_NOTIFICATION_MARK_AS_DONE(request, status ):
    notification = Student_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('student_notification') 



def STUDENT_FEEDBACK(request):
    student_id = Student.objects.get(admin=request.user.id)
    feedback_history = Student_Feedback.objects.filter(student_id=student_id)
    
    context = {
        'feedback_history':feedback_history
    }
    return render(request, 'student/feedback.html', context)




def STUDENT_FEEDBACK_SAVE(request):
    if request.method == 'POST':
        feedback = request.POST.get("feedback")
        student = Student.objects.get(admin=request.user.id)
        
        feedback = Student_Feedback(
            student_id = student,
            feedback = feedback,
            feedback_reply = "",  
        )
        feedback.save()
        return redirect('student_feedback')
    
    
    
    
def STUDENT_LEAVE(request):
    student = Student.objects.get(admin=request.user.id)
    student_leave_history = Student_Leave.objects.filter(student_id=student)
    
    context = {
            'student_leave_history': student_leave_history
        }
    return render(request, 'student/apply_leave.html', context) 




def STUDENT_LEAVE_SAVE(request): 
    if request.method == 'POST':
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')
        
        student_id = Student.objects.get(admin=request.user.id)
        
        student_leave = Student_Leave(
            student_id =student_id,
            data = leave_date,
            message = leave_message
        )
        student_leave.save()
        messages.success(request, 'Leave Are Successfully Sent !')
        
        return redirect('student_leave')  
    
    
    
    
def STUDENT_VIEW_ATTENDANCE(request):
    student = Student.objects.get(admin=request.user.id)
    subjects = Subject.objects.filter(course=student.course_id)
    action = request.GET.get('action')
    
    get_subject = None
    attendance_report = None
    
    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            get_subject = Subject.objects.get(id=subject_id)
            
            attendance_report = Attendance_Report.objects.filter(student_id=student, attendance_id__subject_id=subject_id)
    
    
    context = {
        'subjects': subjects,
        'action': action,
        'get_subject': get_subject,
        'attendance_report': attendance_report
    }
    
    return render(request, 'student/view_attendance.html', context)   




def VIEW_RESULT(request): 
    total_marks = None
    student = Student.objects.get(admin=request.user.id)
    result = StudentResult.objects.filter(student_id=student)
    
    for i in result:
        assignment_mark = i.assignment_mark
        exam_mark = i.exam_mark
        total_marks = assignment_mark + exam_mark
    
    context = {
        'result': result,
        'total_marks': total_marks,
    } 
    
    return render(request, 'student/view_result.html', context)   
    
    
    
    
    
    
    
    
    
    
    
    