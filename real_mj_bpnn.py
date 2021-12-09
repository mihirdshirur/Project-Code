import os
import sys
import optparse
import matplotlib.pyplot as plt
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
import random

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

from sumolib import checkBinary
import traci
Q = []




def get_options():
    opt_parser = optparse.OptionParser()
    opt_parser.add_option("--nogui", action="store_true", default=False, help="run the commandline version of sumo")
    options, args = opt_parser.parse_args()
    return options

def run(thresh1,thresh9,thresh7,thresh4):
    options=get_options()
    
    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')
    
    #sumoBinary = checkBinary('sumo')
    traci.start([sumoBinary, "-c", "real_mj.sumocfg", "--tripinfo-output","tripinfo1.xml"])
    step = 0
    need_yellow1 = 0
    wait_duration1 = 0
    last_traffic_update1 = 0
    need_yellow9 = 0
    wait_duration9 = 0
    last_traffic_update9 = 0
    need_yellow7 = 0
    wait_duration7 = 0
    last_traffic_update7 = 0
    need_yellow4 = 0
    wait_duration4 = 0
    last_traffic_update4 = 0
    
    p11 = 0
    p13 = 0
    p71 = 0
    p73 = 0
    p41 = 0
    p43 = 0
    p91 = 0
    p93 = 0
    q10 = []
    q11 = []
    q12 = []
    q30 = []
    q31 = []
    q32 = []
    q40 = []
    q41 = []
    q42 = []
    q50 = []
    q51 = []
    q52 = []
    q60 = []
    q61 = []
    q62 = []
    q70 = []
    q71 = []
    q72 = []
    q80 = []
    q81 = []
    q82 = []
    q100 = []
    q101 = []
    q102 = []
    q120 = []
    q121 = []
    q122 = []
    q130 = []
    q131 = []
    q132 = []
    q140 = []
    q141 = []
    q142 = []
    q160 = []
    q161 = []
    q162 = []
    q180 = []
    q181 = []
    q182 = []
    q190 = []
    q191 = []
    q192 = []
    q200 = []
    q201 = []
    q202 = []
    q220 = []
    q221 = []
    q222 = []
    wt10 = 0
    wt11 = 0
    wt12 = 0
    wt30 = 0
    wt31 = 0
    wt32 = 0
    wt40 = 0
    wt41 = 0
    wt42 = 0
    wt50 = 0
    wt51 = 0
    wt52 = 0
    wt60 = 0
    wt61 = 0
    wt62 = 0
    wt70 = 0
    wt71 = 0
    wt72 = 0
    wt80 = 0
    wt81 = 0
    wt82 = 0
    wt100 = 0
    wt101 = 0
    wt102 = 0
    wt120 = 0
    wt121 = 0
    wt122 = 0
    wt130 = 0
    wt131 = 0
    wt132 = 0
    wt140 = 0
    wt141 = 0
    wt142 = 0
    wt160 = 0
    wt161 = 0
    wt162 = 0
    wt180 = 0
    wt181 = 0
    wt182 = 0
    wt190 = 0
    wt191 = 0
    wt192 = 0
    wt200 = 0
    wt201 = 0
    wt202 = 0
    wt220 = 0
    wt221 = 0
    wt222 = 0 
    Q10 = 0
    Q11 = 0
    Q12 = 0
    Q30 = 0
    Q31 = 0
    Q32 = 0
    Q40 = 0
    Q41 = 0
    Q42 = 0
    Q50 = 0
    Q51 = 0
    Q52 = 0
    Q60 = 0
    Q61 = 0
    Q62 = 0
    Q70 = 0
    Q71 = 0
    Q72 = 0
    Q80 = 0
    Q81 = 0
    Q82 = 0
    Q100 = 0
    Q101 = 0
    Q102 = 0
    Q120 = 0
    Q121 = 0
    Q122 = 0
    Q130 = 0
    Q131 = 0
    Q132 = 0
    Q140 = 0
    Q141 = 0
    Q142 = 0
    Q160 = 0
    Q161 = 0
    Q162 = 0
    Q180 = 0
    Q181 = 0
    Q182 = 0
    Q190 = 0
    Q191 = 0
    Q192 = 0
    Q200 = 0
    Q201 = 0
    Q202 = 0
    Q220 = 0
    Q221 = 0
    Q222 = 0
                                                                
    
    
    while step<2000:
        '''
        if step%20==0:
            q10.append(Q10) 
            q11.append(Q11)
            q12.append(Q12)
            q30.append(Q30)
            q31.append(Q31) 
            q32.append(Q32) 
            q40.append(Q40)
            q41.append(Q41) 
            q42.append(Q42)
            q50.append(Q50) 
            q51.append(Q51) 
            q52.append(Q52) 
            q60.append(Q60)
            q61.append(Q61) 
            q62.append(Q62)
            q70.append(Q70)
            q71.append(Q71) 
            q72.append(Q72)
            q80.append(Q80) 
            q81.append(Q81) 
            q82.append(Q82) 
            q100.append(Q100) 
            q101.append(Q101) 
            q102.append(Q102)
            q120.append(Q120) 
            q121.append(Q121) 
            q122.append(Q122) 
            q130.append(Q130) 
            q131.append(Q131)
            q132.append(Q132) 
            q140.append(Q140) 
            q141.append(Q141) 
            q142.append(Q142) 
            q160.append(Q160) 
            q161.append(Q161) 
            q162.append(Q162) 
            q180.append(Q180) 
            q181.append(Q181) 
            q182.append(Q182) 
            q190.append(Q190) 
            q191.append(Q191) 
            q192.append(Q192) 
            q200.append(Q200) 
            q201.append(Q201) 
            q202.append(Q202) 
            q220.append(Q220) 
            q221.append(Q221) 
            q222.append(Q222) 
        '''
        traci.simulationStep()
        wt10 = (traci.lane.getWaitingTime("e1_0"))
        wt11 = (traci.lane.getWaitingTime("e1_1"))
        wt12 = (traci.lane.getWaitingTime("e1_2"))
        wt30 = (traci.lane.getWaitingTime("e3_0"))
        wt31 = (traci.lane.getWaitingTime("e3_1"))
        wt32 = (traci.lane.getWaitingTime("e3_2"))
        wt50 = (traci.lane.getWaitingTime("e5_0"))
        wt51 = (traci.lane.getWaitingTime("e5_1"))
        wt52 = (traci.lane.getWaitingTime("e5_2"))
        wt70 = (traci.lane.getWaitingTime("e7_0"))
        wt71 = (traci.lane.getWaitingTime("e7_1"))
        wt72 = (traci.lane.getWaitingTime("e7_2"))
        wt130 = (traci.lane.getWaitingTime("e13_0"))
        wt131 = (traci.lane.getWaitingTime("e13_1"))
        wt132 = (traci.lane.getWaitingTime("e13_2"))
        wt140 = (traci.lane.getWaitingTime("e14_0"))
        wt141 = (traci.lane.getWaitingTime("e14_1"))
        wt142 = (traci.lane.getWaitingTime("e14_2"))
        wt160 = (traci.lane.getWaitingTime("e16_0"))
        wt161 = (traci.lane.getWaitingTime("e16_1"))
        wt162 = (traci.lane.getWaitingTime("e16_2"))
        wt180 = (traci.lane.getWaitingTime("e18_0"))
        wt181 = (traci.lane.getWaitingTime("e18_1"))
        wt182 = (traci.lane.getWaitingTime("e18_2"))
        wt60 = (traci.lane.getWaitingTime("e6_0"))
        wt61 = (traci.lane.getWaitingTime("e6_1"))
        wt62 = (traci.lane.getWaitingTime("e6_2"))
        wt80 = (traci.lane.getWaitingTime("e8_0"))
        wt81 = (traci.lane.getWaitingTime("e8_1"))
        wt82 = (traci.lane.getWaitingTime("e8_2"))
        wt100 = (traci.lane.getWaitingTime("e10_0"))
        wt101 = (traci.lane.getWaitingTime("e10_1"))
        wt102 = (traci.lane.getWaitingTime("e10_2"))
        wt120 = (traci.lane.getWaitingTime("e12_0"))
        wt121 = (traci.lane.getWaitingTime("e12_1"))
        wt122 = (traci.lane.getWaitingTime("e12_2"))
        wt40 = (traci.lane.getWaitingTime("e4_0"))
        wt41 = (traci.lane.getWaitingTime("e4_1"))
        wt42 = (traci.lane.getWaitingTime("e4_2"))
        wt190 = (traci.lane.getWaitingTime("e19_0"))
        wt191 = (traci.lane.getWaitingTime("e19_1"))
        wt192 = (traci.lane.getWaitingTime("e19_2"))
        wt200 = (traci.lane.getWaitingTime("e20_0"))
        wt201 = (traci.lane.getWaitingTime("e20_1"))
        wt202 = (traci.lane.getWaitingTime("e20_2"))
        wt220 = (traci.lane.getWaitingTime("e22_0"))
        wt221 = (traci.lane.getWaitingTime("e22_1"))
        wt222 = (traci.lane.getWaitingTime("e22_2"))

        Q10 = traci.lanearea.getLastStepVehicleNumber("det_1_0")
        Q11 = traci.lanearea.getLastStepVehicleNumber("det_1_1")
        Q12 = traci.lanearea.getLastStepVehicleNumber("det_1_2")
        Q30 = traci.lanearea.getLastStepVehicleNumber("det_3_0")
        Q31 = traci.lanearea.getLastStepVehicleNumber("det_3_1")
        Q32 = traci.lanearea.getLastStepVehicleNumber("det_3_2")
        Q40 = traci.lanearea.getLastStepVehicleNumber("det_4_0")
        Q41 = traci.lanearea.getLastStepVehicleNumber("det_4_1")
        Q42 = traci.lanearea.getLastStepVehicleNumber("det_4_2")
        Q50 = traci.lanearea.getLastStepVehicleNumber("det_5_0")
        Q51 = traci.lanearea.getLastStepVehicleNumber("det_5_1")
        Q52 = traci.lanearea.getLastStepVehicleNumber("det_5_2")
        Q60 = traci.lanearea.getLastStepVehicleNumber("det_6_0")
        Q61 = traci.lanearea.getLastStepVehicleNumber("det_6_1")
        Q62 = traci.lanearea.getLastStepVehicleNumber("det_6_2")
        Q70 = traci.lanearea.getLastStepVehicleNumber("det_7_0")
        Q71 = traci.lanearea.getLastStepVehicleNumber("det_7_1")
        Q72 = traci.lanearea.getLastStepVehicleNumber("det_7_2")
        Q80 = traci.lanearea.getLastStepVehicleNumber("det_8_0")
        Q81 = traci.lanearea.getLastStepVehicleNumber("det_8_1")
        Q82 = traci.lanearea.getLastStepVehicleNumber("det_8_2")
        Q100 =traci.lanearea.getLastStepVehicleNumber("det_10_0")
        Q101 =traci.lanearea.getLastStepVehicleNumber("det_10_1")
        Q102 =traci.lanearea.getLastStepVehicleNumber("det_10_2")
        Q120 =traci.lanearea.getLastStepVehicleNumber("det_12_0")
        Q121 =traci.lanearea.getLastStepVehicleNumber("det_12_1")
        Q122 = traci.lanearea.getLastStepVehicleNumber("det_12_2")
        Q130 = traci.lanearea.getLastStepVehicleNumber("det_13_0")
        Q131 = traci.lanearea.getLastStepVehicleNumber("det_13_1")
        Q132 = traci.lanearea.getLastStepVehicleNumber("det_13_2")
        Q140 = traci.lanearea.getLastStepVehicleNumber("det_14_0")
        Q141 = traci.lanearea.getLastStepVehicleNumber("det_14_1")
        Q142 = traci.lanearea.getLastStepVehicleNumber("det_14_2")
        Q160 = traci.lanearea.getLastStepVehicleNumber("det_16_0")
        Q161 = traci.lanearea.getLastStepVehicleNumber("det_16_1")
        Q162 = traci.lanearea.getLastStepVehicleNumber("det_16_2")
        Q180 = traci.lanearea.getLastStepVehicleNumber("det_18_0")
        Q181 = traci.lanearea.getLastStepVehicleNumber("det_18_1")
        Q182 = traci.lanearea.getLastStepVehicleNumber("det_18_2")
        Q190 = traci.lanearea.getLastStepVehicleNumber("det_19_0")
        Q191 = traci.lanearea.getLastStepVehicleNumber("det_19_1")
        Q192 = traci.lanearea.getLastStepVehicleNumber("det_19_2")
        Q200 = traci.lanearea.getLastStepVehicleNumber("det_20_0")
        Q201 = traci.lanearea.getLastStepVehicleNumber("det_20_1")
        Q202 = traci.lanearea.getLastStepVehicleNumber("det_20_2")
        Q220 = traci.lanearea.getLastStepVehicleNumber("det_22_0")
        Q221 = traci.lanearea.getLastStepVehicleNumber("det_22_1")
        Q222 = traci.lanearea.getLastStepVehicleNumber("det_22_2")
        Q.append(Q10+Q11+Q12+Q30+Q31+Q32+Q40+Q41+Q42+Q50+Q51+Q52+Q60+Q61+Q62+Q70+Q71+Q72+Q80+Q81+Q82+Q100+Q101+Q102+Q120+Q121+Q122+Q130+Q131+Q132+Q140+Q141+Q142+Q160+Q161+Q162+Q180+Q181+Q182+Q190+Q191+Q192+Q200+Q201+Q202+Q220+Q221+Q222)
        Q_4 = (Q40+Q41+Q42)/3
        Q_5 = (Q50+Q51+Q52)/3
        Q_6 = (Q60+Q61+Q62)/3
        Q_7 = (Q70+Q71+Q72)/3
        Q_12 = (Q120+Q121+Q122)/3
        Q_13 = (Q130+Q131+Q132)/3
        Q_18 = (Q180+Q181+Q182)/3
        Q_19 = (Q190+Q191+Q192)/3
        #j1_tl = j1_tl + traci.multientryexit.getLastIntervalMeanTimeLoss("e3_J1_e1") + traci.multientryexit.getLastIntervalMeanTimeLoss("e3_J1_e3") + traci.multientryexit.getLastIntervalMeanTimeLoss("e3_J1_e5") + traci.multientryexit.getLastIntervalMeanTimeLoss("e3_J1_e7")
        #j4_tl = j4_tl + traci.multientryexit.getLastIntervalMeanTimeLoss("e3_J1_e19") + traci.multientryexit.getLastIntervalMeanTimeLoss("e3_J1_e20") + traci.multientryexit.getLastIntervalMeanTimeLoss("e3_J1_e22") + traci.multientryexit.getLastIntervalMeanTimeLoss("e3_J1_e4")
        #j9_tl = j9_tl + traci.multientryexit.getLastIntervalMeanTimeLoss("e3_J1_e10") + traci.multientryexit.getLastIntervalMeanTimeLoss("e3_J1_e12") + traci.multientryexit.getLastIntervalMeanTimeLoss("e3_J1_e6") + traci.multientryexit.getLastIntervalMeanTimeLoss("e3_J1_e8")
        #j7_tl = j7_tl + traci.multientryexit.getLastIntervalMeanTimeLoss("e3_J1_e13") + traci.multientryexit.getLastIntervalMeanTimeLoss("e3_J1_e14") + traci.multientryexit.getLastIntervalMeanTimeLoss("e3_J1_e16") + traci.multientryexit.getLastIntervalMeanTimeLoss("e3_J1_e18")
        # Calculate backpressure for junction 1
        p1 = [0,0,0,0]
        r1 = [0,0,0,0]
        p1[0] = (Q10 + Q11 - Q_4) + (Q50 + Q51 - Q_6)
        r1[0] = (wt10 + wt11 + wt50 + wt51)/4
        p1[1] = (Q12 - Q_6) + (Q52)
        r1[1] = (wt12 + wt52)/2
        p1[2] = (Q30 + Q31 - Q_4 - Q_6) + (Q70 + Q71)
        r1[2] = (wt30 + wt31 + wt70 + wt71)/4
        p1[3] = (Q32) + (Q72 - Q_4)
        r1[3] = (wt32 + wt72)/2
        # Calculate backpressure for junction 9
        p9 = [0,0,0,0] 
        r9 = [0,0,0,0]
        p9[0] = (Q80 + Q81 - Q_13 - Q_7) + (Q120 + Q121)
        r9[0] = (wt80 + wt81 + wt120 + wt121)/4
        p9[1] = (Q82) + (Q122 - Q_7)
        r9[1] = (wt82 + wt122)/2
        p9[2] = (Q60 + Q61 - Q_13) + (Q100 + Q101 - Q_7)
        r9[2] = (wt60 + wt61 + wt100 + wt101)/4
        p9[3] = (Q62) + (Q102 - Q_13)
        r9[3] = (wt62 + wt102)/2
        # Calculate backpressure and red light time for junction 7
        p7 = [0,0,0,0]
        r7 = [0,0,0,0]
        p7[0] = (Q130 + Q131 - Q_19) + (Q160 + Q161 - Q_12)
        r7[0] = (wt130 + wt131 + wt160 + wt161)/4
        p7[1] = (Q132) + (Q162 - Q_19)
        r7[1] = (wt132 + wt162)/2
        p7[2] = (Q180 + Q181) + (Q140 + Q141 - Q_19)
        r7[2] = (wt180 + wt181 + wt140 + wt141)/4
        p7[3] = (Q182 - Q_12) + (Q142)
        r7[3] = (wt182 + wt142)/2
        # Calculate backpressure and red light time for junction 4
        p4 = [0,0,0,0]
        r4 = [0,0,0,0]
        p4[0] = (Q40 + Q41) + (Q200 + Q201 - Q_18 - Q_5)
        r4[0] = (wt40 + wt41 + wt200 + wt201)/4
        p4[1] = (Q42 - Q_18) + (Q202)
        r4[1] = (wt42 + wt202)/2
        p4[2] = (Q220 + Q221 - Q_18) + (Q190 + Q191 - Q_5)
        r4[2] = (wt220 + wt221 + wt190 + wt191)/4
        p4[3] = (Q222 - Q_5) + (Q192)
        r4[3] = (wt222 + wt192)/2

        # Compute phase for junction 1
      
        if max(r1) < thresh1: 
            phase1 = p1.index(max(p1))
        else:
            phase1 = r1.index(max(r1))
        # Compute phase for junction 9
       
        if max(r9) < thresh9:
            
            phase9 = p9.index(max(p9))
        else:
           
            phase9 = r9.index(max(r9))
        # Compute phase for junction 7
 
        if max(r7) < thresh7:
            phase7 = p7.index(max(p7))
        else:
            
            phase7 = r9.index(max(r9))
        # Compute phase for junction 4
   
        if max(r4) < thresh4:
            
            phase4 = p4.index(max(p4))
        else:
            
            phase4 = r9.index(max(r9))


        if (need_yellow1!=0)and(step==(last_traffic_update1+wait_duration1)):
            traci.trafficlight.setPhase("J1",need_yellow1)
            last_traffic_update1 = step
            wait_duration1 = 1
            need_yellow1 = 0
        if (phase1 == 0)and(step==(last_traffic_update1+wait_duration1)):
            traci.trafficlight.setPhase("J1",4)
            last_traffic_update1 = step
            wait_duration1 = 12
            need_yellow1 = 5
        if (phase1 == 1)and(step==(last_traffic_update1+wait_duration1)):
            p11 = p11 + 1
            if p11%3==0:
                traci.trafficlight.setPhase("J1",4)
                last_traffic_update1 = step
                wait_duration1 = 12
                need_yellow1 = 5
                
            else:
                traci.trafficlight.setPhase("J1",6)
                last_traffic_update1 = step
                wait_duration1 = 12
                need_yellow1 = 7
        if (phase1 == 2)and(step==(last_traffic_update1+wait_duration1)):
            traci.trafficlight.setPhase("J1",0)
            last_traffic_update1 = step
            wait_duration1 = 12
            need_yellow1 = 1
        if (phase1 == 3)and(step==(last_traffic_update1+wait_duration1)):
            p13 = p13 + 1
            if p13%3==0:
                traci.trafficlight.setPhase("J1",0)
                last_traffic_update1 = step
                wait_duration1 = 12
                need_yellow1 = 1
            else:
                traci.trafficlight.setPhase("J1",2)
                last_traffic_update1 = step
                wait_duration1 = 12
                need_yellow1 = 3


        if (need_yellow9!=0)and(step==(last_traffic_update9+wait_duration9)):
            traci.trafficlight.setPhase("J9",need_yellow9)
            last_traffic_update9 = step
            wait_duration9 = 1
            need_yellow9 = 0
        if (phase9 == 0)and(step==(last_traffic_update9+wait_duration9)):
            traci.trafficlight.setPhase("J9",4)
            last_traffic_update9 = step
            wait_duration9 = 12
            need_yellow9 = 5
        if (phase9 == 1)and(step==(last_traffic_update9+wait_duration9)):
            p91 = p91 + 1
            if p91%3==0:
                traci.trafficlight.setPhase("J9",4)
                last_traffic_update9 = step
                wait_duration9 = 12
                need_yellow9 = 5
            else:
                traci.trafficlight.setPhase("J9",6)
                last_traffic_update9 = step
                wait_duration9 = 12
                need_yellow9 = 7
        if (phase9 == 2)and(step==(last_traffic_update9+wait_duration9)):
            traci.trafficlight.setPhase("J9",0)
            last_traffic_update9 = step
            wait_duration9 = 12
            need_yellow9 = 1
        if (phase9 == 3)and(step==(last_traffic_update9+wait_duration9)):
            p93 = p93 + 1
            if p93%3==0:
                traci.trafficlight.setPhase("J9",0)
                last_traffic_update9 = step
                wait_duration9 = 12
                need_yellow9 = 1
                
            else:
                traci.trafficlight.setPhase("J9",2)
                last_traffic_update9 = step
                wait_duration9 = 12
                need_yellow9 = 3


        if (need_yellow7!=0)and(step==(last_traffic_update7+wait_duration7)):
            traci.trafficlight.setPhase("J7",need_yellow7)
            last_traffic_update7 = step
            wait_duration7 = 1
            need_yellow7 = 0
        if (phase7 == 0)and(step==(last_traffic_update7+wait_duration7)):
            traci.trafficlight.setPhase("J7",4)
            last_traffic_update7 = step
            wait_duration7 = 12
            need_yellow7 = 5
        if (phase7 == 1)and(step==(last_traffic_update7+wait_duration7)):
            p71 = p71 + 1
            if p71%3==0:
                traci.trafficlight.setPhase("J7",4)
                last_traffic_update7 = step
                wait_duration7 = 12
                need_yellow7 = 5
            else:
                traci.trafficlight.setPhase("J7",6)
                last_traffic_update7 = step
                wait_duration7 = 12
                need_yellow7 = 7
        if (phase7 == 2)and(step==(last_traffic_update7+wait_duration7)):
            traci.trafficlight.setPhase("J7",0)
            last_traffic_update7 = step
            wait_duration7 = 12
            need_yellow7 = 1
        if (phase7 == 3)and(step==(last_traffic_update7+wait_duration7)):
            p73 = p73 + 1
            if p73%3==0:
                traci.trafficlight.setPhase("J7",0)
                last_traffic_update7 = step
                wait_duration7 = 12
                need_yellow7 = 1
            else:
                traci.trafficlight.setPhase("J7",2)
                last_traffic_update7 = step
                wait_duration7 = 12
                need_yellow7 = 3

      
        if (need_yellow4!=0)and(step==(last_traffic_update4+wait_duration4)):
            traci.trafficlight.setPhase("J4",need_yellow4)
            last_traffic_update4 = step
            wait_duration4 = 1
            need_yellow4 = 0
        if (phase4 == 0)and(step==(last_traffic_update4+wait_duration4)):
            traci.trafficlight.setPhase("J4",4)
            last_traffic_update4 = step
            wait_duration4 = 12
            need_yellow4 = 5
        if (phase4 == 1)and(step==(last_traffic_update4+wait_duration4)):
            p41 = p41 + 1
            if p41%3==0:
                traci.trafficlight.setPhase("J4",4)
                last_traffic_update4 = step
                wait_duration4 = 12
                need_yellow4 = 5
            else:
                traci.trafficlight.setPhase("J4",6)
                last_traffic_update4 = step
                wait_duration4 = 12
                need_yellow4 = 7
        if (phase4 == 2)and(step==(last_traffic_update4+wait_duration4)):
            traci.trafficlight.setPhase("J4",0)
            last_traffic_update4 = step
            wait_duration4 = 12
            need_yellow4 = 1
        if (phase4 == 3)and(step==(last_traffic_update4+wait_duration4)):
            p43 = p43 + 1
            if p43%3==0:
                traci.trafficlight.setPhase("J4",0)
                last_traffic_update4 = step
                wait_duration4 = 12
                need_yellow4 = 1
            else:
                traci.trafficlight.setPhase("J4",2)
                last_traffic_update4 = step
                wait_duration4 = 12
                need_yellow4 = 3

        
        step = step + 1
    
    print(thresh1,thresh9,thresh7,thresh4)
    traci.close()
    return Q
    

if __name__=="__main__":
    
    
    '''
    for i in range(10):
        t1 = random.randint(0,2)
        t2 = random.randint(0,2)
        t3 = random.randint(0,2)
        t4 = random.randint(0,2)
        
        for j in range(10):
            n = random.randint(1,10)
            l = [10*n-5,10*n,10*n+5]
            run(l[t1],l[t2],l[t3],l[t4])
    '''
    sys.stdout.flush()
    Q = run(80,80,80,80)
    x=[]
    Q1 = []
    x1 = []
    for i in range(2000):
        x.append(i)
    for j in range(0,2000,25):
        Q1.append(Q[j])
        x1.append(x[j])

    plt.scatter(x1,Q1)
    plt.xlabel("Time Step(s)")
    plt.ylabel("Total Q Length(m)")
    plt.title("Stability of Network (1 per sec)")
    plt.legend()
    plt.show()
    
    
    
    
        
               
        
        

        


        

        
