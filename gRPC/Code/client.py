
#!/usr/bin/python

from concurrent import futures # for threadpool
import os
import sys
import time
import threading

import grpc
import student
import student_pb2
import student_pb2_grpc


class Client(object):
    """ Client class for interacting with student gRPC server"""

    def close(self, channel):
        self.channel.close()
        return

    def run(self):
        self.channel = grpc.insecure_channel("localhost:9999")
        stub = student_pb2_grpc.StudentRegistryStub(self.channel)
        try:
            while True:
                print ("[*] Press 1 to add new student record")
                print ("[*] Press 2 to fetch a student record")
                print ("[*] Press 3 to remove student record")
                x = input()
                try:
                    option = int(x)
                    if not (1 <= option <= 3):
                        raise ValueError()
                except ValueError as ve:
                    print ("[#] {} is not a valid option".format(x))
                    continue
                if (option == 1):
                    print ("\t[*] Adding Student: ")
                    name = input("\t\tStudent Name: ")
                    try:
                        cls = int(input("\t\tStudent Class (integer): "))
                    except Exception:
                        cls = 0
                    response = stub.addStudent(student_pb2.student(name=name,cls=cls))
                    print ("\t[*] Student successfully added with {}".format(response))

                elif (option == 2):
                    studId = input("\t[*] Fetching Student record with ID: ")
                    try:
                        studId = int(studId)
                    except ValueError as ve:
                        print ("[#] Error:{} StudentId must be numeric ".format(studId))

                    studentObj = stub.getStudent(student_pb2.studentId(studentId=studId))
                    if (studentObj.cls == -1):
                        print ("No student with Id = {} present".format(studId))
                        print ()
                    else:
                        print (studentObj)

                elif (option == 3):
                    studId = input("\t[*] Removing Student record with ID: ")
                    try:
                        studId = int(studId)
                    except ValueError as ve:
                        print ("[#] Error:{} StudentId must be numeric ".format(studId))

                    studentObj = stub.removeStudent(student_pb2.studentId(studentId=studId))
                    if (studentObj.cls == -1):
                        print ("No student with Id = {} present".format(studId))
                        print ()
                    else:
                        print (studentObj)
                else:
                    print ("[#] {} is not a valid option".format(option))
        except Exception as e:
            print ("[#] Error: run()", e)
            self.channel.unsubscribe(self.close)
            sys.exit(1)



if __name__ == "__main__":
    Client().run()
