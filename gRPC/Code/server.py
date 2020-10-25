
#!/usr/bin/python

from concurrent import futures # for threadpool
import sys
import time
import threading

import grpc
from student import (
        Student,
        StudentRecords
        )
        
import student_pb2
import student_pb2_grpc


class grpcListener(student_pb2_grpc.StudentRegistryServicer):
    """ gRPC listener for server side processing"""

    def __init__(self, *args, **kwargs):
        self._sr = StudentRecords.getInstance()

    def addStudent(self, request, context):
        studId = self._sr.addStudent(request.name, request.cls)
        return student_pb2.studentId(studentId=studId)

    def getStudent(self, request, context):
        studId = request.studentId
        studentObj = self._sr.getStudent(studId)
        if studentObj:
            return student_pb2.student(name=studentObj.name, cls=studentObj.cls)
        else:
            return student_pb2.student(name="", cls=-1)

    def removeStudent(self, request, context):
        studId = request.studentId
        studentObj = self._sr.removeStudent(studId)
        if studentObj:
            return student_pb2.student(name=studentObj.name, cls=studentObj.cls)
        else:
            return student_pb2.student(name="", cls="")

def main(argv):
    num_threads = 1
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=num_threads))
    student_pb2_grpc.add_StudentRegistryServicer_to_server(grpcListener(), server)
    server.add_insecure_port("[::]:9999")
    server.start()
    try:
        while True:
            print ("[*] Server running {} threads".format(threading.active_count()))
            time.sleep(2)
    except KeyboardInterrupt as ke:
        print ("[#] Close signal..")
        server.stop(0)


if __name__ == "__main__":
    main(sys.argv)
