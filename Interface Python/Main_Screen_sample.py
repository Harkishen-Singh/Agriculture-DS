# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_Screen.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
transferControl = False

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(737, 596)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 170, 201, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 240, 231, 211))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(440, 230, 231, 201))
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(370, 230, 20, 181))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 510, 94, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 40, 601, 101))
        self.label_4.setObjectName("label_4")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(430, 510, 31, 31))
        self.commandLinkButton.setText("")
        self.commandLinkButton.setObjectName("commandLinkButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Agriculture Growth Prediction, Machine Learning"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Designed and Developed By :</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'Helvetica, sans-serif\'; font-size:12pt; font-weight:600; color:#000000;\">Pratik srichandan </span></p><p align=\"center\"><span style=\" font-family:\'Helvetica, sans-serif\'; font-size:8pt; color:#000000;\">M.Tech ,CSE<br/>College of Engineering &amp; Technology,BBSR</span></p><p align=\"center\"><span style=\" font-family:\'Helvetica, sans-serif\'; color:#000000;\">pratiksrichandan1991@gmail.com</span></p><p><br/></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'Helvetica, sans-serif\'; font-size:12pt; font-weight:600; color:#000000;\">Harkishen Singh</span></p><p align=\"center\"><span style=\" font-family:\'Helvetica, sans-serif\'; font-size:small; color:#000000;\">B.Tech, CSE<br/>College of Engineering &amp; Technology,BBSR</span></p><p align=\"center\"><span style=\" font-family:\'Helvetica, sans-serif\'; font-size:12pt; color:#000000;\">harkishensingh@hotmail.com</span></p><p"))
        self.pushButton.setText(_translate("MainWindow", "Next"))

        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:16pt; font-weight:600; color:#000000;\">DATA ANALYTICS AND PREDICTION</span></p><p align=\"center\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:16pt; font-weight:600; color:#000000;\">IN AGRICULTURAL GROWTH</span></p><p><span style=\" font-size:16pt;\"><br/></span></p></body></html>"))
        self.pushButton.clicked.connect(self.response)

    def response(self):
        transferControl = True

        MainWindow.destroy()
        print('Reached here')

        self.Form2 = QtWidgets.QWidget()
        '''ui = Ui_Form()
        ui.setupUi(Form2)'''
        self.setupUi2(self.Form2)

        #sys.exit(app2.exec_())


#class Ui_Form(object):
    def setupUi2(self, Form2):
        self.Form2.setObjectName("Form")
        self.Form2.resize(753, 576)
        self.label = QtWidgets.QLabel(self.Form2)
        self.label.setGeometry(QtCore.QRect(20, 10, 231, 31))
        self.label.setObjectName("label")
        self.breiefDesp = QtWidgets.QTextBrowser(self.Form2)
        self.breiefDesp.setGeometry(QtCore.QRect(20, 50, 711, 471))
        self.breiefDesp.setDocumentTitle("")
        self.breiefDesp.setObjectName("breiefDesp")
        self.pushButton2 = QtWidgets.QPushButton(self.Form2)
        self.pushButton2.setGeometry(QtCore.QRect(633, 530, 101, 36))
        self.pushButton2.setObjectName("pushButton2")

        self.retranslateUi2(self.Form2)
        QtCore.QMetaObject.connectSlotsByName(self.Form2)

    def retranslateUi2(self, Form2):
        _translate = QtCore.QCoreApplication.translate
        self.Form2.setWindowTitle(_translate("Form", "Agriculture - Description"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Brief Description</span></p></body></html>"))
        self.breiefDesp.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:\'Times New Roman,serif\'; font-weight:600; color:#000000;\">1.INTRODUCTION</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; font-family:\'Times New Roman,serif\'; font-weight:600; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt; color:#000000;\">There has been much research and various attempts to apply new Data science &amp; analytics technology to agricultural areas. However, Data science &amp; analytics for the agriculture should be considered differently against the same areas such as industrial, logistics.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" font-family:\'Calibri,sans-serif\'; color:#000000;\">Methods of harvest forecasting have become increasingly elaborate. Highly refined statistical techniques in agriculture are now being used to extract information from past data and to project prediction values of economic variables. To a large extent, these advances in the science of harvest forecasting have been made possible by progress in IT technology. But, solitary statistical techniques do not provide perfect future situation. Therefore, it is necessary to analyze correlating monitoring crop environments with statistical information about harvest. It is expected that from Data science &amp; analytics -based decision support system, this information on statistical pattern of crop can be obtained. The purpose of this study is to improve the agricultural forecast supporting information system, so that real-time forecast will be possible . To this end, it will be needed to manage IoT devices and gather information on them more appropriately. The IoT sensor based agricultural production System consists of three parts: relation analysis and statistical prediction. This system is designed an agricultural decision support system to predict crop growth by monitoring periodically using the IoT sensor technology.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-weight:600; color:#000000;\">2.LITERATURE SURVEY</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:\'Times New Roman, serif\'; color:#000000;\">[1]Pradnya S. Borkar :-This paper is about sensor based water pumping where the sensor senses the moisture of the soil and pumps water to the field according to it. Here LCD and GSM receive the information about temperature, humidity and conditions of the soil and motor. Soil moisture sensor sense the condition of the soil whether it is dry or wet and sends the information to microcontroller. The main controlling device is microcontroller. Soil sensor will give the status of the soil to the microcontroller, based on that microcontroller will display the status of the soil on the LCD and switch on or off the pumping motor through relay.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%;\"><span style=\" font-family:\'Calibri,sans-serif\'; color:#000000;\">[2]Vidadala Srija et.al..:-This project shows the implementation of agricultural automation system using WEB and GSM technologies. Optimum usage of water is main objective of this system. Here temperature, soil moisture and water level can be monitored on web page through micro controller and information will be send by SMS. This page contains all the information about the status of the sensors. This information will be viewed at remote location by using GPRS technology. Automation of Irrigation System Using ANN based Controller described a simple approach to Irrigation control problem using Artificial Neural Network Controller. The proposed system is compared with ON/OFF </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%;\"><span style=\" font-family:\'Calibri,sans-serif\'; color:#000000;\">[3]Muhammad et al :-In this paper a simple approach to more efficient irrigation technique using artificial intelligence neural network controller. The proposed system is compared with ON/OFF controller and it is shown that ON/OFF Controller based System fails miserably because of its limitations of time delay it can’t give appropriate value within specified time. On the other hand ANN based approach has resulted in possible implementation of better and more efficient control .This paper depends on different types of parameter like root level , wind direction, soil saltiness etc. for more efficient decision. These controllers do not require a prior knowledge of system and have inherent ability to adapt to the changing conditions unlike conventional methods. It is noteworthy that ANN based systems can save lot of energy and water and can provide optimized results.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" color:#000000;\"><br /></span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%;\"><span style=\" font-family:\'Calibri,sans-serif\'; color:#000000;\">[4]Prathyusha.K:-Main purpose of this paper to reduce the wastage of water by using real time irrigation technique . It provides provide exact controlling of field by using the drip irrigation, atomizing the agricultural environment by using the components to implement this proposed system ARM LPC2148 Microcontroller is used . ARM LPC2148 Microcontroller and GSM are used for the automation of drip irrigation and also to monitor the field and gives the accurate results to the end user i.e to the farmer. By using this real time irrigation a farmer can reduce the water wastage upto 50 percent. MCU-based home wireless control centre is used along with one WSN centre node module and several data collecting nodes, GSM module, GSM network and mobile phone. The WSN data collecting node modules are connected with different types of sensors.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%;\"><span style=\" font-family:\'Calibri,sans-serif\'; color:#000000;\">[5]Pratibha Gangurde :-Due to popularity of wireless sensors networks and their wide spread use over military , agriculture, industry . Here in this paper the author observed different kind of used technology in agriculture and comparing them over different types of sensor used , different interface used for the sensors , their protocols use for communication . The brief categorization of used technology is very effective to know the limitations of the existing models and to get the effective model which can lead to the optimal solution and increase the production in agriculture. The Precision agriculture system performs various operations like sensing agricultural parameters , Identification of sensing location and data gathering, actuation and Control decision based on sensed data etc. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%;\"><span style=\" font-family:\'Calibri,sans-serif\'; color:#000000;\">[6].Akash Jain et al.:- In this paper remote monitoring systems using wireless protocols used by different researchers for betterment of agricultural yield is discussed. Some of the reviews are done on different papers N.G saha’s soil moisture monitoring system for précised irrigation, in some other studies related to agriculture in wireless sensor network researches measures different parameters collected from sensors .The proposed model of the author works on the XBEE module for the transfer data over network in real time and FPGA elements are used for monitoring the data.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:\'Times New Roman, serif\'; color:#000000;\">[7]GopalaKrishna Moorthy .K:-The main purpose of this paper is to develop a smart wireless sensors networks for agriculture enviorment .The proposed system is divided into three parts field side , server side , client side .The hardware circuit used in the field side used to get the parameters via sensors . The collected data is transferred by a Zigbee module .The collected data in server side are saved in excel format and transferred with the help of mobile data . The client side securely stores the received data for future use for real time data use it uses drop box synchronization . </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%;\"><span style=\" font-family:\'Calibri,sans-serif\'; color:#000000;\">[8]Prof. R. K. Moje:- This paper focuses on different crops that need different parameters of water , temperature , soil moisture etc. Here a wireless sensor network based on Zigbee/IEEE802.15.4 standard is utilized as a weather station network sending weather information . For better processing microcontroller LPC2138 32 bit embedded RISC processor is used. The Physical and media access layer are used for low data rate wireless personal area network .The frequency band supports different data gross rate .The sensed data are transmitted to receiver side via zigbee module through Tx and Rx pin and the recived data used for precision .</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%;\"><span style=\" font-family:\'Calibri,sans-serif\'; color:#000000;\">[9]Ion Ionescu de la Brad:- The problem faced by the agriculture industry can be solved by using Artificial intelligence in agriculture . This paper focuses on expert system , artificial agent on agriculture , sensor for data collection , developing robots for agriculture purpose . This paper is mainly on literature survey and the data collected statistically .The author conducted Exploratory trials of 64 software and online expert systems for agriculture. The outcome from this was it is not happening for insufficiency of reliable data and systematic data which can be overcome by using intelligent agent in agriculture in farm level .</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%;\"><span style=\" font-family:\'Calibri,sans-serif\'; color:#000000;\">[10]Miss.Snehal S.Dahikar:- This paper explains how local climate in India affects agriculture due to wrong selection of crop in respect of the climate . Artificial intelligence is used and with the help of the data gathered from the environment is analyzed and a suitable crop is choose to produce more crop . In this model the back propagation algorithm (Rumelhart and McClelland, 1986) is used in layered feed-forward ANNs is used which propagates the signal in forward direction and propagate the error in backward direction. By collecting the error and minimizing the chance of error this model gradually leads to ward optimal solution , from the collected data and by pattern matching technique it refers the more efficient crop in that climate condition .</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman, serif\'; color:#000000;\">[11]Shaik Jhani Bhasha:- In this paper the author implemented a prototype of a mechanism using PIC16F877A microcontroller. This peripheral interface controller is used because of its low cost , wide availability , serial program capability and its reprogrammable flash memory function .The water level when reaches the required level the microcontroller senses it and activates the relay driver to switch OFF the motor if it turned of because of some reason the GSM modem sends it via a message to the user by which the user can send a ON message to the controller to switch it on . This is an effective way to minimize the burden of watering the agriculture field.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman, serif\'; color:#000000;\">[12]Rakesh Patel:- The author describes how cloud computing can positively impact on agriculture sector, where the end user that is farmers do not require to know anything about the service he/she is getting but the farmer can get the service by different categories of cloud computing services such as SAAS, PAAS , IAAS . Some of the examples of enhancement of agriculture by the help of cloud computing described like Cloud agro service , e-data bank, e-knowledge sharing where the farmer can get help from any part of the country which can give an instant solution to the end user, some times the user can interact with the expert to by the help of live conversation . A term Gandhi Engineering as cloud computing provides low cost , high operational efficiency , elasticity and scalability .</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%;\"><span style=\" font-family:\'Calibri,sans-serif\'; color:#000000;\">[13]B. MiloviC:- In this paper how data mining is implemented to access the large scale of agriculture related data in a effective manner . It describes the way of data classification and regression such as Association rules, Cluster analysis ,text mining task , Link analysis task and the different types of data mining techniques are used which can help to get the searched data are Artificial neural network ,Condition tree , nearest neighborhood method , Genetic algorithm. Data mining technique helps in comparing yield , taking decision , setting average production by comparing. This paper also describes the difficulties hidden with it like for data mining electronic records are needed which need consistent monitoring to gather the data and the main problem with it is the agriculture data is vast and heterogeneous in nature. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:\'Times New Roman, serif\'; color:#000000;\">[14].Anup Vibhute: Here author describes the use image processing for the purpose of analysis of agriculture field. As the time taken by the expert user to get the required result can be reduced by using this technique. RS data and pattern recognition technique was used to estimate direct and independent crop area in the study region , Visual techniques based on FCC (False Color Composite) were generated at different bands and were assigned with blue, green and red colors where as the digital techniques applied to each pixel and use full dynamic range of observations were preferred for crop discrimination .The author compared many other papers and gave a brief knowledge about the workings principle and describing the effective use of techniques to get optimized result . </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:\'Calibri,sans-serif\'; color:#000000;\">[15].M. P. Raj :</span><span style=\" font-family:\'Calibri,sans-serif\'; color:#252525;\"> This paper explores employment of pattern recognition in an agricultural domain. The pattern recognition deals with the automatic discoveries of regularities in data using computer algorithm . Basic steps of pattern recognition process which are defined in this process are Processing , Feature Extraction , Feature Selection classification and decision making . The different pattern recognition modes like Statistical model , syntactical model , Template matching , Neural network. The training data given is both in target values and without target values which helps to classify the similar data and categories them , so the explain model uses both supervised model and unsupervised model for input data classification and to provide desired solution to the problem .Different papers are reviewed and their techniques used in farming or agriculture are discussed .</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%;\"><span style=\" font-family:\'Calibri,sans-serif\'; color:#000000;\">[16].YETHIRAJ N G: In this paper some techniques of data mining techniques are explained such as ID3 algorithms, the k-means, the k nearest neighbor, artificial neural networks and support vector machines in the field of agriculture . This paper describes a project that is applying a range of machine learning strategies to problems in agriculture and horticulture . The author briefly surveyed the techniques emerged from machine learning to set a workbench for experimenting with a verity of techniques. A case study of interpreting paddy distributions of three counties on Northern Taiwan during two crop seasons on year 2000 using multi-temporal imageries together with cadastre GIS by Bayesian posteriori probability classifier was also studied. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:\'Calibri,sans-serif\'; color:#000000;\">[17]Veena Divya: The author in this paper used android based software platform for automated irrigation control system .The microcontroller and GSM modules are connected through MAX232 .At required situations the microcontroller gives signal to called mobile which is in auto answering mode and then it interacts with the valve to communicate and do the necessary operation like opening and closing the valve. The minimum power supply should be +5 V. Drip irrigation system is used here as in minimize the loss of water and it is effective in maximize the yield . These are applications written in Java. Some of basic applications include an calendar, email client, SMS program, maps, making phone calls, accessing the Web browser, accessing your contacts list and others. The basic architecture works with the Applications, application frame work , libraries , linux kernel and baseband.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:\'Times New Roman, serif\'; color:#000000;\">[18]Surabhi Singh : The basic idea behind this paper is to study the flow of data through a wireless transmission making use of wireless sensor network and monitoring system. Various paper are studied to measure the different attributes of soil like moisture, water flux, conductivity, etc . The system layout is discussed in both top-down and bottom –up approach . The total system is designed in Six layers those are the technical details, data processing and manipulation, sensing and indication are considered in Requirement level , the detailed assessment of system requirements are analyzed in Specification level , Architecture level deals with the hardware partition, performance and analysis. , Component level work with both hardware and software component , Integration level integrates all the hardware and software components together and builds a structural network. , in Application level the system developed is implemented to the agricultural field and the task of precise monitoring and control is carried out for maintain the crop quality and production.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:\'Times New Roman, serif\'; color:#000000;\">[19].Sweeti. A. Parwatkar: This paper presents the use of zigbee wireless technology in automated irrigation management system which uses wireless sensor networks. Zigbee carries some advantages like being of low cost, low power and wireless mesh topology networking standard. The objective Of the System is to conserve energy &amp; water resources.To handles the system manually and automatically. Different types of irrigation methods are explained here such as surface irrigation, micro irrigation methods and their sub categories . In this paper classification of existing systems are done where brief description of Zigbee, Bluetooth LE, Wavenis, Insteon, Enocean, UWB are done and the proposed system is given on the basis of best outcome by analyzing them. .</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:\'Times New Roman, serif\'; color:#000000;\">[20]Chetana A. Kestikar: In this paper the author made a user friendly and efficient automated wireless watering system. The user interface for this system is developed using C# in .NET Framework 3.5. For the microcontroller and other hardware programming embedded C in AVR Studio is used. The system architecture is divided in two parts the PC side and the hardware components on the field. Different hardware which were used are described. This system uses both manual and automatic mode of operation. Thr message containing ‘$S’ is sent to the microcontroller via GSM Modem through the program and before it displays to the user ‘/’ acts as a splitter which helps to recognize the values. The system also provides the log file of the events carried out.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:\'Calibri,sans-serif\'; color:#000000;\">[21]Alaa Rahhoom Hadi: This paper emphasizes on this issue and resolves the issues and gives the Automated techniques are the best solution for minimizing the power, reduce waste of water and increase the efficiency. In this system Information is exchanged between far end and designed system via GPRS module. MAX232 is used to connect the GSM module and microcontroller. The zone of the plant, a root is put a wetted profile where the little amount of water lead to deep percolation this is the main merits of this technique. A solenoid valves an electromechanically operated valve. The valve is controlled by an electric current through a solenoid . The Android operation system which was written with Java language using the Android Software Development kit (SDK). A multi-language software is used known as eclipse. A long enough pipe is used which is helpful to reach the roots and the operation is controlled by the solenoid valve.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:\'Times New Roman, serif\'; color:#000000;\">[22]ARUNA.P : The purpose of this paper is to provide more facility in agriculture field by using Zigbee. The project describes an application of a wireless sensor network for low-cost wireless monitored and controlled irrigation. there are two Microcontroller units, one unit is placed in agricultural field and the other unit is placed in main control unit which is interfaced with motor unit .The author described many existing systems and their working . The proposed system where the zigbee itself acts as a receiver and transmitter channel . The design process of the proposed system is Device specification , Architecture and component . The observed humidity and moisture sensors are within the fixed level the motor is in off condition and the LCD display shows the &quot;OFF” condition of motor , when Irrigation System is ON then the value of crop Temperature, humidity, Soil moisture crossed the fixed value then buzzer gets ON and displays on master node LCD and PC.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%;\"><span style=\" font-family:\'Calibri,sans-serif\'; color:#000000;\">[23]Dr. D.K.Sreekantha: Automation of farming practices has proved to increase the food production levels. This paper surveys the work carried out by various researchers to get a holistic picture on current state of implementation of automation in agricultural practices around the world. The author describes different challenges in agriculture such as Small and scattered land holdings, Affordability and financing of farm equipment, Poor quality levels of equipment procurement mechanism and poor after sales service etc. Here the author studied different papers and explained the working principles and various technique they used.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%;\"><span style=\" font-family:\'Calibri,sans-serif\'; color:#000000;\">[24]S.S.Katariya: The author explains the four major work in agriculture field which is done by a robot without giving any human support. The robot still running on a white track they are given a delay after equal interval of time and at that equal interval of time the robot stop and do the operation of 1) Pesticide spraying 2) Dropping the seed’s 3) Ploughing 4) Providing water to crop. The controlled action according to output of comparator which followed by different equation . This paper is only works in linear path food farming it is not possible for the crop field where white line is not possible.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:\'Times New Roman, serif\'; color:#000000;\">[25]Muhammad Umair:- This paper represents Artificial Neural Network (ANN) based intelligent control system for effective irrigation scheduling . The proposed Artificial Neural Network (ANN) based controller have prototyped using MATLAB .The procedure of irrigation is described in two ways open loop controller and closed loop controller both the ways uses physical parameter for the purpose of irrigation. Input parameters like temperature , humidity ,wind speed and radiation which directly influence the procedure of irrigation which is expressed by the Penman method is updated by FAO .The control unit consist of artificial neural network which which supervises the amount of water which should be supplied in order to optimized the whole system.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:\'Times New Roman, serif\'; color:#000000;\">[26]. R.Revathi :- This paper explained an irrigation system using microcontroller, GSM module and a moisture sensor, which helps in providing an effective and reliable irrigation system. The system was built with single chip 80C51 module and GTM900C GPRS (General Packet Radio Service) module. The major objectives of the proposed system are low cost and effective with less power consumption using sensors for remote monitoring and controlling devices which are controlled via SMS using a GSM module. The system works with a GSM FLYSCALE SIM900 module and Arduino Uno microcontroller and a moisture sensor. The command signals from the user are obtained as messages from the user by the GSM module. This GSM module converts the message into hexadecimal code so that the microcontroller could process it.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%;\"><span style=\" font-family:\'Calibri,sans-serif\'; color:#000000;\">[27]Shriyash Thawali: This paper represents a robot capable of performing operations like automatic ploughing, seed dispensing and pesticide spraying. Control of this agro-bot will be wireless. Design and analyze a real time system for these robot give a solution and proposed a model which can be used in real time field. the robot Analyzed the design of plough tool and developed for real time system. The robotic system is built using high torque DC motor, communication module, relay driver circuit, Battery package, microcontroller. The mechanical parts of the robot are designed with the help of Pro-E Design Software. By the help of this type of robot the author tried to minimize some problem in agriculture field .</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:\'Times New Roman, serif\'; color:#000000;\">[28]Gaurav Jadhav : In this paper raspberry-pi is taken as main board and sensors collect s all the real time data from environment and this real time data is fetched by the web server and display it. The systems mentioned in this paper are active in achieving the purpose of collecting sensor data and storing them over server . The in-built features of MySQL servers, namely Triggers Delimiters, using these features of MySQL, expected data ranges can be specified in the database table. The collected data from all the nodes are collected, this information is transmitted to a local base station (ATmega 128) through multi-hop transmission. API for the Internet of Things that enables users to collect, store, analyze, visualize, and act on data from sensors or actuators. Here author created a ThingSpeak channels store data sent to them from apps or devices. API keys enable users to write data to a channel or read data from a private channel.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:\'Calibri,sans-serif\'; color:#000000;\">[29]Jaideep Nuvvula : This paper proposed a monitoring unit for Controlled Environment Agriculture (CEA) that is designed using the state-of-art hardware specifications and multiple sensors. The proposed device can be readily used in practice in the Hydroponics environment and has great potential for other applications like green house agriculture, vertical farming. The CEA’s System provides automated control and monitoring program . This proposed work offer ease of use, effective and reliable control system. The proposed system is modelled using Arduino development kit which connects to light sensor measuring the light intensity, environment temperature/humidity sensor for getting the and humidity in the surroundings, soil moisture sensor for volumetric water level, and air toxicity measuring carbon monoxide and oxygen levels. The results obtained from the device have indicated that the performance is well, especially in collecting, logging and analyzing the sporadic data from the sensors that is transferred to central node for farmers’ use.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:\'Times New Roman, serif\'; color:#000000;\">[30]Christoph Husemann: This paper aims on the deduction of a concrete FMIS from a general Farm Management Information Systems (FMIS). The concrete FMIS has to focus on the needs of medium-sized and multifunctional farms. FMIS accurately display all branches of the farm at hand, so that the newly developed FMIS represents a valuable tool for the farmer to successfully manage the farm. The main objective of this paper is planning , organizing ,monitoring , controlling . The authors reviewed historical and contemporary literature to analyze different general ISs. The analyzed case study farm is a good example of such a complex farm structure. the case-study farm has three major braches, namely “Plant Production”, “Services” and “Livestock Production”. The branch “Plant Production”. The case-study farm emphasizes on an easy adaptation, user-friendliness, and accuracy in depicting the various production processes and services</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:\'Times New Roman, serif\'; color:#000000;\">[31]Bishnu Deo Kumar: In this paper automatic irrigation which is controlled by the ATMEGA 328 which keep track of the fluctuation in the environment by the help of sensors . Ardunio is used for the coding .The microcontroller senses the signal by the help of OP AMP comparator which acts as a interface between the sensing arrangements and the microcontroller . This system keep track of the both temperature and humidity of the soil which provide the detail data about the requirement of the field . This leads to a enhanced irrigation process and reducing the pressure of the farmer .</span></p></body></html>"))
        self.pushButton2.setText(_translate("Form", "Next"))
        self.pushButton2.clicked.connect(self.response2)
        self.Form2.show()

    def response2(self):
        a=0
        self.Form2.destroy()
        #from Interface.InputFormat import Ui_Form

        self.Form3 = QtWidgets.QWidget()
        '''ui = Ui_Form()
        ui.setupUi(Form2)'''
        self.setupUi3(self.Form3)

    def setupUi3(self, Form3):
        self.Form3.setObjectName("Form")
        self.Form3.resize(718, 533)
        self.pushButton = QtWidgets.QPushButton(self.Form3)
        self.pushButton.setGeometry(QtCore.QRect(260, 120, 201, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.Form3)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 210, 201, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.Form3)
        self.label.setGeometry(QtCore.QRect(170, 70, 351, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Form3)
        self.label_2.setGeometry(QtCore.QRect(310, 330, 201, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.Form3)
        self.lineEdit.setGeometry(QtCore.QRect(210, 290, 301, 34))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi3(self.Form3)
        QtCore.QMetaObject.connectSlotsByName(self.Form3)

    def retranslateUi3(self, Form3):
        _translate = QtCore.QCoreApplication.translate
        self.Form3.setWindowTitle(_translate("Form", "Input Format"))
        self.pushButton.setText(_translate("Form", "Single Input "))
        self.pushButton_2.setText(_translate("Form", "Multi Input through .CSV"))
        self.label.setText(_translate("Form", "Select Input Format to help us Predict the Conditions"))
        self.label_2.setText(_translate("Form", "*if Multi Input Option Selected"))
        self.lineEdit.setText(_translate("Form", "Name of the .csv file (without extension)"))
        self.Form3.show()

        self.pushButton.clicked.connect(self.responseToAsker)
        self.pushButton_2.clicked.connect(self.responseToMulti)

    def responseToAsker(self):  ## points to provoking the asker.py file
        self.Form3.destroy()
        self.Form4 = QtWidgets.QWidget()
        self.setupUi4(self.Form4)


    def setupUi4(self, Form4):
        self.Form4.setObjectName("Form4")
        self.Form4.resize(753, 545)
        self.label = QtWidgets.QLabel(self.Form4)
        self.label.setGeometry(QtCore.QRect(10, 10, 191, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Form4)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 111, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.Form4)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 111, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.Form4)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 161, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.Form4)
        self.label_5.setGeometry(QtCore.QRect(20, 140, 161, 20))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.Form4)
        self.pushButton.setGeometry(QtCore.QRect(630, 480, 94, 36))
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(self.Form4)
        self.label_6.setGeometry(QtCore.QRect(20, 170, 141, 20))
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox(self.Form4)
        self.comboBox.setGeometry(QtCore.QRect(180, 110, 161, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.Form4)
        self.comboBox_2.setGeometry(QtCore.QRect(180, 140, 161, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.Form4)
        self.comboBox_3.setGeometry(QtCore.QRect(180, 170, 161, 21))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(self.Form4)
        self.comboBox_4.setGeometry(QtCore.QRect(180, 200, 161, 21))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_7 = QtWidgets.QLabel(self.Form4)
        self.label_7.setGeometry(QtCore.QRect(20, 200, 141, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.Form4)
        self.label_8.setGeometry(QtCore.QRect(20, 230, 141, 20))
        self.label_8.setObjectName("label_8")
        self.comboBox_5 = QtWidgets.QComboBox(self.Form4)
        self.comboBox_5.setGeometry(QtCore.QRect(180, 230, 161, 21))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.line = QtWidgets.QFrame(self.Form4)
        self.line.setGeometry(QtCore.QRect(10, 30, 711, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_9 = QtWidgets.QLabel(self.Form4)
        self.label_9.setGeometry(QtCore.QRect(20, 269, 141, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.Form4)
        self.label_10.setGeometry(QtCore.QRect(360, 270, 131, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.Form4)
        self.label_11.setGeometry(QtCore.QRect(20, 310, 141, 31))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.Form4)
        self.label_12.setGeometry(QtCore.QRect(360, 320, 101, 20))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.Form4)
        self.label_13.setGeometry(QtCore.QRect(20, 360, 141, 21))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.Form4)
        self.label_14.setGeometry(QtCore.QRect(360, 360, 81, 20))
        self.label_14.setObjectName("label_14")
        self.lineEdit = QtWidgets.QLineEdit(self.Form4)
        self.lineEdit.setGeometry(QtCore.QRect(180, 80, 541, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Form4)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 50, 541, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.Form4)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 260, 161, 34))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.Form4)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 310, 161, 34))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.Form4)
        self.lineEdit_5.setGeometry(QtCore.QRect(180, 360, 161, 34))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.retranslateUi4(self.Form4)
        QtCore.QMetaObject.connectSlotsByName(self.Form4)

    def retranslateUi4(self, Form4):
        _translate = QtCore.QCoreApplication.translate
        self.Form4.setWindowTitle(_translate("Form4", "Agriculture Prediction Model"))
        self.label.setText(_translate("Form4", "Input the Values"))
        self.label_2.setText(_translate("Form4", "Block Name :"))
        self.label_3.setText(_translate("Form4", "Variety Name "))
        self.label_4.setText(_translate("Form4", "System Of Cultivation"))
        self.label_5.setText(_translate("Form4", "Sources Of Seed "))
        self.pushButton.setText(_translate("Form4", "Submit"))
        self.label_6.setText(_translate("Form4", "Is Field Irrigated"))
        self.comboBox.setItemText(0, _translate("Form4", " Conventional"))
        self.comboBox.setItemText(1, _translate("Form4", " SRi"))
        self.comboBox_2.setItemText(0, _translate("Form4", " Own Source"))
        self.comboBox_2.setItemText(1, _translate("Form4", " Departmental Source"))
        self.comboBox_2.setItemText(2, _translate("Form4", " Private Source"))
        self.comboBox_3.setItemText(0, _translate("Form4", " Irrigated"))
        self.comboBox_3.setItemText(1, _translate("Form4", " Un-irrigated"))
        self.comboBox_3.setItemText(2, _translate("Form4", " Rainfed"))
        self.comboBox_3.setItemText(3, _translate("Form4", " No"))
        self.comboBox_4.setItemText(0, _translate("Form4", " High Yielding Variety"))
        self.comboBox_4.setItemText(1, _translate("Form4", " Local"))
        self.comboBox_4.setItemText(2, _translate("Form4", " Hybrid"))
        self.label_7.setText(_translate("Form4", "Crop Variety Type"))
        self.label_8.setText(_translate("Form4", "Water Source"))
        self.comboBox_5.setItemText(0, _translate("Form4", " Canal"))
        self.comboBox_5.setItemText(1, _translate("Form4", " Submersible Pump"))
        self.comboBox_5.setItemText(2, _translate("Form4", " Tank"))
        self.comboBox_5.setItemText(3, _translate("Form4", " None"))
        self.comboBox_5.setItemText(4, _translate("Form4", " Other"))
        self.label_9.setText(_translate("Form4", "Damage by Pests"))
        self.label_10.setText(_translate("Form4", "Numeric Value"))
        self.label_11.setText(_translate("Form4", "Operational Size holding"))
        self.label_12.setText(_translate("Form4", "In hectares"))
        self.label_13.setText(_translate("Form4", "Area Under Crop"))
        self.label_14.setText(_translate("Form4", "In hectares"))
        self.Form4.show()


    def responseToMulti(self): ## points to multi caller
        self.Form3.destroy()
        self.Form5 = QtWidgets.QWidget()
        self.setupUi5(self.Form5)

    def setupUi5(self, Form):
        self.Form5.setObjectName("Form")
        self.Form5.resize(747, 537)
        self.pushButton = QtWidgets.QPushButton(self.Form5)
        self.pushButton.setGeometry(QtCore.QRect(240, 450, 271, 36))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.Form5)
        self.label.setGeometry(QtCore.QRect(50, 30, 631, 371))
        self.label.setObjectName("label")

        self.retranslateUi5(self.Form5)
        QtCore.QMetaObject.connectSlotsByName(self.Form5)

    def retranslateUi5(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.Form5.setWindowTitle(_translate("Form", "Multi Input through .csv"))
        self.pushButton.setText(_translate("Form", "Yes, It has the required columns"))
        self.label.setText(_translate("Form", "Make sure, your csv file has the following heading as the columns headings:\n"
        "\n"
        "variety name\n"
        "system of cultivation\n"
        "is irrigated\n"
        "yielding type\n"
        "pest damage\n"
        "seeds per hectare\n"
        "operation size\n"
        "cultivation size"))
        self.Form5.show()

if __name__ == "__main__":
    import sys
    #app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())






