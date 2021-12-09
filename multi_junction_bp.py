import os
import sys
import optparse
import matplotlib.pyplot as plt
from statistics import mean

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

from sumolib import checkBinary
import traci


def get_options():
    opt_parser = optparse.OptionParser()
    opt_parser.add_option("--nogui", action="store_true", default=False, help="run the commandline version of sumo")
    options, args = opt_parser.parse_args()
    return options

def run():
    step = 0
    need_yellow1 = 0
    wait_duration1 = 0
    last_traffic_update1 = 0
    need_yellow2 = 0
    wait_duration2 = 0
    last_traffic_update2 = 0
    need_yellow3 = 0
    wait_duration3 = 0
    last_traffic_update3 = 0
    need_yellow4 = 0
    wait_duration4 = 0
    last_traffic_update4 = 0
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
    q70 = []
    q71 = []
    q72 = []
    q90 = []
    q91 = []
    q92 = []
    q100 = []
    q101 = []
    q102 = []
    q110 = []
    q111 = []
    q112 = []
    q130 = []
    q131 = []
    q132 = []
    q150 = []
    q151 = []
    q152 = []
    q160 = []
    q161 = []
    q162 = []
    q170 = []
    q171 = []
    q172 = []
    q190 = []
    q191 = []
    q192 = []
    q210 = []
    q211 = []
    q212 = []
    q220 = []
    q221 = []
    q222 = []
    q230 = []
    q231 = []
    q232 = []
    jl10 = []
    jl11 = []
    jl12 = []
    jl30 = []
    jl31 = []
    jl32 = []
    jl40 = []
    jl41 = []
    jl42 = []
    jl50 = []
    jl51 = []
    jl52 = []
    jl70 = []
    jl71 = []
    jl72 = []
    jl90 = []
    jl91 = []
    jl92 = []
    jl100 = []
    jl101 = []
    jl102 = []
    jl110 = []
    jl111 = []
    jl112 = []
    jl130 = []
    jl131 = []
    jl132 = []
    jl150 = []
    jl151 = []
    jl152 = []
    jl160 = []
    jl161 = []
    jl162 = []
    jl170 = []
    jl171 = []
    jl172 = []
    jl190 = []
    jl191 = []
    jl192 = []
    jl210 = []
    jl211 = []
    jl212 = []
    jl220 = []
    jl221 = []
    jl222 = []
    jl230 = []
    jl231 = []
    jl232 = []
    ms10 = []
    ms11 = []
    ms12 = []
    ms30 = []
    ms31 = []
    ms32 = []
    ms40 = []
    ms41 = []
    ms42 = []
    ms50 = []
    ms51 = []
    ms52 = []
    ms70 = []
    ms71 = []
    ms72 = []
    ms90 = []
    ms91 = []
    ms92 = []
    ms100 = []
    ms101 = []
    ms102 = []
    ms110 = []
    ms111 = []
    ms112 = []
    ms130 = []
    ms131 = []
    ms132 = []
    ms150 = []
    ms151 = []
    ms152 = []
    ms160 = []
    ms161 = []
    ms162 = []
    ms170 = []
    ms171 = []
    ms172 = []
    ms190 = []
    ms191 = []
    ms192 = []
    ms210 = []
    ms211 = []
    ms212 = []
    ms220 = []
    ms221 = []
    ms222 = []
    ms230 = []
    ms231 = []
    ms232 = []
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
    Q70 = 0
    Q71 = 0
    Q72 = 0
    Q90 = 0
    Q91 = 0
    Q92 = 0
    Q100 =0
    Q101 =0
    Q102 =0
    Q110 =0
    Q111 =0
    Q112 = 0
    Q130 = 0
    Q131 = 0
    Q132 = 0
    Q150 = 0
    Q151 = 0
    Q152 = 0
    Q160 = 0
    Q161 = 0
    Q162 = 0
    Q170 = 0
    Q171 = 0
    Q172 = 0
    Q190 = 0
    Q191 = 0
    Q192 = 0
    Q210 = 0
    Q211 = 0
    Q212 = 0
    Q220 = 0
    Q221 = 0
    Q222 = 0
    Q230 = 0
    Q231 = 0
    Q232 = 0
    JL10 = 0
    JL11 = 0
    JL12 = 0
    JL30 = 0
    JL31 = 0
    JL32 = 0
    JL40 = 0
    JL41 = 0
    JL42 = 0
    JL50 = 0
    JL51 = 0
    JL52 = 0
    JL70 = 0
    JL71 = 0
    JL72 = 0
    JL90 = 0
    JL91 = 0
    JL92 = 0
    JL100 =0
    JL101 =0
    JL102 =0
    JL110 =0
    JL111 =0
    JL112 = 0
    JL130 = 0
    JL131 = 0
    JL132 = 0
    JL150 = 0
    JL151 = 0
    JL152 = 0
    JL160 = 0
    JL161 = 0
    JL162 = 0
    JL170 = 0
    JL171 = 0
    JL172 = 0
    JL190 = 0
    JL191 = 0
    JL192 = 0
    JL210 = 0
    JL211 = 0
    JL212 = 0
    JL220 = 0
    JL221 = 0
    JL222 = 0
    JL230 = 0
    JL231 = 0
    JL232 = 0
    MS10 = 0
    MS11 = 0
    MS12 = 0
    MS30 = 0
    MS31 = 0
    MS32 = 0
    MS40 = 0
    MS41 = 0
    MS42 = 0
    MS50 = 0
    MS51 = 0
    MS52 = 0
    MS70 = 0
    MS71 = 0
    MS72 = 0
    MS90 = 0
    MS91 = 0
    MS92 = 0
    MS100 = 0
    MS101 = 0
    MS102 = 0
    MS110 = 0
    MS111 = 0
    MS112 = 0
    MS130 = 0
    MS131 = 0
    MS132 = 0
    MS150 = 0
    MS151 = 0
    MS152 = 0
    MS160 = 0
    MS161 = 0
    MS162 = 0
    MS170 = 0
    MS171 = 0
    MS172 = 0
    MS190 = 0
    MS191 = 0
    MS192 = 0
    MS210 = 0
    MS211 = 0
    MS212 = 0
    MS220 = 0
    MS221 = 0
    MS222 = 0
    MS230 = 0
    MS231 = 0
    MS232 = 0
    
    while step<1000:
        if step%50==0:
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
            q70.append(Q70)
            q71.append(Q71) 
            q72.append(Q72)
            q90.append(Q90) 
            q91.append(Q91) 
            q92.append(Q92) 
            q100.append(Q100) 
            q101.append(Q101) 
            q102.append(Q102)
            q110.append(Q110) 
            q111.append(Q111) 
            q112.append(Q112) 
            q130.append(Q130) 
            q131.append(Q131)
            q132.append(Q132) 
            q150.append(Q150) 
            q151.append(Q151) 
            q152.append(Q152) 
            q160.append(Q160) 
            q161.append(Q161) 
            q162.append(Q162) 
            q170.append(Q170) 
            q171.append(Q171) 
            q172.append(Q172) 
            q190.append(Q190) 
            q191.append(Q191) 
            q192.append(Q192) 
            q210.append(Q210) 
            q211.append(Q211) 
            q212.append(Q212) 
            q220.append(Q220) 
            q221.append(Q221) 
            q222.append(Q222) 
            q230.append(Q230) 
            q231.append(Q231) 
            q232.append(Q232) 
            jl10.append(JL10) 
            jl11.append(JL11)
            jl12.append(JL12)
            jl30.append(JL30)
            jl31.append(JL31) 
            jl32.append(JL32) 
            jl40.append(JL40)
            jl41.append(JL41) 
            jl42.append(JL42)
            jl50.append(JL50) 
            jl51.append(JL51) 
            jl52.append(JL52) 
            jl70.append(JL70)
            jl71.append(JL71) 
            jl72.append(JL72)
            jl90.append(JL90) 
            jl91.append(JL91) 
            jl92.append(JL92) 
            jl100.append(JL100) 
            jl101.append(JL101) 
            jl102.append(JL102)
            jl110.append(JL110) 
            jl111.append(JL111) 
            jl112.append(JL112) 
            jl130.append(JL130) 
            jl131.append(JL131)
            jl132.append(JL132) 
            jl150.append(JL150) 
            jl151.append(JL151) 
            jl152.append(JL152) 
            jl160.append(JL160) 
            jl161.append(JL161) 
            jl162.append(JL162) 
            jl170.append(JL170) 
            jl171.append(JL171) 
            jl172.append(JL172) 
            jl190.append(JL190) 
            jl191.append(JL191) 
            jl192.append(JL192) 
            jl210.append(JL210) 
            jl211.append(JL211) 
            jl212.append(JL212) 
            jl220.append(JL220) 
            jl221.append(JL221) 
            jl222.append(JL222) 
            jl230.append(JL230) 
            jl231.append(JL231) 
            jl232.append(JL232) 
            ms10.append(MS10) 
            ms11.append(MS11)
            ms12.append(MS12)
            ms30.append(MS30)
            ms31.append(MS31) 
            ms32.append(MS32) 
            ms40.append(MS40)
            ms41.append(MS41) 
            ms42.append(MS42)
            ms50.append(MS50) 
            ms51.append(MS51) 
            ms52.append(MS52) 
            ms70.append(MS70)
            ms71.append(MS71) 
            ms72.append(MS72)
            ms90.append(MS90) 
            ms91.append(MS91) 
            ms92.append(MS92) 
            ms100.append(MS100) 
            ms101.append(MS101) 
            ms102.append(MS102)
            ms110.append(MS110) 
            ms111.append(MS111) 
            ms112.append(MS112) 
            ms130.append(MS130) 
            ms131.append(MS131)
            ms132.append(MS132) 
            ms150.append(MS150) 
            ms151.append(MS151) 
            ms152.append(MS152) 
            ms160.append(MS160) 
            ms161.append(MS161) 
            ms162.append(MS162) 
            ms170.append(MS170) 
            ms171.append(MS171) 
            ms172.append(MS172) 
            ms190.append(MS190) 
            ms191.append(MS191) 
            ms192.append(MS192) 
            ms210.append(MS210) 
            ms211.append(MS211) 
            ms212.append(MS212) 
            ms220.append(MS220) 
            ms221.append(MS221) 
            ms222.append(MS222) 
            ms230.append(MS230) 
            ms231.append(MS231) 
            ms232.append(MS232) 
        traci.simulationStep()
        MS10 = traci.lanearea.getJamLengthMeters("det_1_0")
        MS11 = traci.lanearea.getJamLengthMeters("det_1_1")
        MS12 = traci.lanearea.getJamLengthMeters("det_1_2")
        MS30 = traci.lanearea.getJamLengthMeters("det_3_0")
        MS31 = traci.lanearea.getJamLengthMeters("det_3_1")
        MS32 = traci.lanearea.getJamLengthMeters("det_3_2")
        MS40 = traci.lanearea.getJamLengthMeters("det_4_0")
        MS41 = traci.lanearea.getJamLengthMeters("det_4_1")
        MS42 = traci.lanearea.getJamLengthMeters("det_4_2")
        MS50 = traci.lanearea.getJamLengthMeters("det_5_0")
        MS51 = traci.lanearea.getJamLengthMeters("det_5_1")
        MS52 = traci.lanearea.getJamLengthMeters("det_5_2")
        MS70 = traci.lanearea.getJamLengthMeters("det_7_0")
        MS71 = traci.lanearea.getJamLengthMeters("det_7_1")
        MS72 = traci.lanearea.getJamLengthMeters("det_7_2")
        MS90 = traci.lanearea.getJamLengthMeters("det_9_0")
        MS91 = traci.lanearea.getJamLengthMeters("det_9_1")
        MS92 = traci.lanearea.getJamLengthMeters("det_9_2")
        MS100 =traci.lanearea.getJamLengthMeters("det_10_0")
        MS101 =traci.lanearea.getJamLengthMeters("det_10_1")
        MS102 =traci.lanearea.getJamLengthMeters("det_10_2")
        MS110 =traci.lanearea.getJamLengthMeters("det_11_0")
        MS111 =traci.lanearea.getJamLengthMeters("det_11_1")
        MS112 = traci.lanearea.getJamLengthMeters("det_11_2")
        MS130 = traci.lanearea.getJamLengthMeters("det_13_0")
        MS131 = traci.lanearea.getJamLengthMeters("det_13_1")
        MS132 = traci.lanearea.getJamLengthMeters("det_13_2")
        MS150 = traci.lanearea.getJamLengthMeters("det_15_0")
        MS151 = traci.lanearea.getJamLengthMeters("det_15_1")
        MS152 = traci.lanearea.getJamLengthMeters("det_15_2")
        MS160 = traci.lanearea.getJamLengthMeters("det_16_0")
        MS161 = traci.lanearea.getJamLengthMeters("det_16_1")
        MS162 = traci.lanearea.getJamLengthMeters("det_16_2")
        MS170 = traci.lanearea.getJamLengthMeters("det_17_0")
        MS171 = traci.lanearea.getJamLengthMeters("det_17_1")
        MS172 = traci.lanearea.getJamLengthMeters("det_17_2")
        MS190 = traci.lanearea.getJamLengthMeters("det_19_0")
        MS191 = traci.lanearea.getJamLengthMeters("det_19_1")
        MS192 = traci.lanearea.getJamLengthMeters("det_19_2")
        MS210 = traci.lanearea.getJamLengthMeters("det_21_0")
        MS211 = traci.lanearea.getJamLengthMeters("det_21_1")
        MS212 = traci.lanearea.getJamLengthMeters("det_21_2")
        MS220 = traci.lanearea.getJamLengthMeters("det_22_0")
        MS221 = traci.lanearea.getJamLengthMeters("det_22_1")
        MS222 = traci.lanearea.getJamLengthMeters("det_22_2")
        MS230 = traci.lanearea.getJamLengthMeters("det_23_0")
        MS231 = traci.lanearea.getJamLengthMeters("det_23_1")
        MS232 = traci.lanearea.getJamLengthMeters("det_23_2")
        JL10 = traci.lanearea.getJamLengthMeters("det_1_0")
        JL11 = traci.lanearea.getJamLengthMeters("det_1_1")
        JL12 = traci.lanearea.getJamLengthMeters("det_1_2")
        JL30 = traci.lanearea.getJamLengthMeters("det_3_0")
        JL31 = traci.lanearea.getJamLengthMeters("det_3_1")
        JL32 = traci.lanearea.getJamLengthMeters("det_3_2")
        JL40 = traci.lanearea.getJamLengthMeters("det_4_0")
        JL41 = traci.lanearea.getJamLengthMeters("det_4_1")
        JL42 = traci.lanearea.getJamLengthMeters("det_4_2")
        JL50 = traci.lanearea.getJamLengthMeters("det_5_0")
        JL51 = traci.lanearea.getJamLengthMeters("det_5_1")
        JL52 = traci.lanearea.getJamLengthMeters("det_5_2")
        JL70 = traci.lanearea.getJamLengthMeters("det_7_0")
        JL71 = traci.lanearea.getJamLengthMeters("det_7_1")
        JL72 = traci.lanearea.getJamLengthMeters("det_7_2")
        JL90 = traci.lanearea.getJamLengthMeters("det_9_0")
        JL91 = traci.lanearea.getJamLengthMeters("det_9_1")
        JL92 = traci.lanearea.getJamLengthMeters("det_9_2")
        JL100 =traci.lanearea.getJamLengthMeters("det_10_0")
        JL101 =traci.lanearea.getJamLengthMeters("det_10_1")
        JL102 =traci.lanearea.getJamLengthMeters("det_10_2")
        JL110 =traci.lanearea.getJamLengthMeters("det_11_0")
        JL111 =traci.lanearea.getJamLengthMeters("det_11_1")
        JL112 = traci.lanearea.getJamLengthMeters("det_11_2")
        JL130 = traci.lanearea.getJamLengthMeters("det_13_0")
        JL131 = traci.lanearea.getJamLengthMeters("det_13_1")
        JL132 = traci.lanearea.getJamLengthMeters("det_13_2")
        JL150 = traci.lanearea.getJamLengthMeters("det_15_0")
        JL151 = traci.lanearea.getJamLengthMeters("det_15_1")
        JL152 = traci.lanearea.getJamLengthMeters("det_15_2")
        JL160 = traci.lanearea.getJamLengthMeters("det_16_0")
        JL161 = traci.lanearea.getJamLengthMeters("det_16_1")
        JL162 = traci.lanearea.getJamLengthMeters("det_16_2")
        JL170 = traci.lanearea.getJamLengthMeters("det_17_0")
        JL171 = traci.lanearea.getJamLengthMeters("det_17_1")
        JL172 = traci.lanearea.getJamLengthMeters("det_17_2")
        JL190 = traci.lanearea.getJamLengthMeters("det_19_0")
        JL191 = traci.lanearea.getJamLengthMeters("det_19_1")
        JL192 = traci.lanearea.getJamLengthMeters("det_19_2")
        JL210 = traci.lanearea.getJamLengthMeters("det_21_0")
        JL211 = traci.lanearea.getJamLengthMeters("det_21_1")
        JL212 = traci.lanearea.getJamLengthMeters("det_21_2")
        JL220 = traci.lanearea.getJamLengthMeters("det_22_0")
        JL221 = traci.lanearea.getJamLengthMeters("det_22_1")
        JL222 = traci.lanearea.getJamLengthMeters("det_22_2")
        JL230 = traci.lanearea.getJamLengthMeters("det_23_0")
        JL231 = traci.lanearea.getJamLengthMeters("det_23_1")
        JL232 = traci.lanearea.getJamLengthMeters("det_23_2")
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
        Q70 = traci.lanearea.getLastStepVehicleNumber("det_7_0")
        Q71 = traci.lanearea.getLastStepVehicleNumber("det_7_1")
        Q72 = traci.lanearea.getLastStepVehicleNumber("det_7_2")
        Q90 = traci.lanearea.getLastStepVehicleNumber("det_9_0")
        Q91 = traci.lanearea.getLastStepVehicleNumber("det_9_1")
        Q92 = traci.lanearea.getLastStepVehicleNumber("det_9_2")
        Q100 =traci.lanearea.getLastStepVehicleNumber("det_10_0")
        Q101 =traci.lanearea.getLastStepVehicleNumber("det_10_1")
        Q102 =traci.lanearea.getLastStepVehicleNumber("det_10_2")
        Q110 =traci.lanearea.getLastStepVehicleNumber("det_11_0")
        Q111 =traci.lanearea.getLastStepVehicleNumber("det_11_1")
        Q112 = traci.lanearea.getLastStepVehicleNumber("det_11_2")
        Q130 = traci.lanearea.getLastStepVehicleNumber("det_13_0")
        Q131 = traci.lanearea.getLastStepVehicleNumber("det_13_1")
        Q132 = traci.lanearea.getLastStepVehicleNumber("det_13_2")
        Q150 = traci.lanearea.getLastStepVehicleNumber("det_15_0")
        Q151 = traci.lanearea.getLastStepVehicleNumber("det_15_1")
        Q152 = traci.lanearea.getLastStepVehicleNumber("det_15_2")
        Q160 = traci.lanearea.getLastStepVehicleNumber("det_16_0")
        Q161 = traci.lanearea.getLastStepVehicleNumber("det_16_1")
        Q162 = traci.lanearea.getLastStepVehicleNumber("det_16_2")
        Q170 = traci.lanearea.getLastStepVehicleNumber("det_17_0")
        Q171 = traci.lanearea.getLastStepVehicleNumber("det_17_1")
        Q172 = traci.lanearea.getLastStepVehicleNumber("det_17_2")
        Q190 = traci.lanearea.getLastStepVehicleNumber("det_19_0")
        Q191 = traci.lanearea.getLastStepVehicleNumber("det_19_1")
        Q192 = traci.lanearea.getLastStepVehicleNumber("det_19_2")
        Q210 = traci.lanearea.getLastStepVehicleNumber("det_21_0")
        Q211 = traci.lanearea.getLastStepVehicleNumber("det_21_1")
        Q212 = traci.lanearea.getLastStepVehicleNumber("det_21_2")
        Q220 = traci.lanearea.getLastStepVehicleNumber("det_22_0")
        Q221 = traci.lanearea.getLastStepVehicleNumber("det_22_1")
        Q222 = traci.lanearea.getLastStepVehicleNumber("det_22_2")
        Q230 = traci.lanearea.getLastStepVehicleNumber("det_23_0")
        Q231 = traci.lanearea.getLastStepVehicleNumber("det_23_1")
        Q232 = traci.lanearea.getLastStepVehicleNumber("det_23_2")
        Q_4 = (Q40+Q41+Q42)/3
        Q_5 = (Q50+Q51+Q52)/3
        Q_10 = (Q100+Q101+Q102)/3
        Q_11 = (Q110+Q111+Q112)/3
        Q_16 = (Q160+Q161+Q162)/3
        Q_17 = (Q170+Q171+Q172)/3
        Q_22 = (Q220+Q221+Q222)/3
        Q_23 = (Q230+Q231+Q232)/3


        p1 = [0,0,0,0]
        p1[0] = Q10 + Q11 - Q_4 + Q50 - Q_23 + Q51
        p1[1] = (Q12 - Q_23 + Q52)
        p1[2] = Q30 - Q_4 + Q31 - Q_23 + Q220 + Q221
        p1[3] = (Q32 - Q_4 + Q222)
        S_p1 = -1000
        p01 = 0
            
        for i in range(4):
            S_temp1 = p1[i]
            if S_temp1 >= S_p1:
                p01 = i
                S_p1 = S_temp1
            
        p2 = [0,0,0,0]
        p2[0] = Q40 + Q41 + Q90 - Q_10 + Q91 - Q_5
        p2[1] = (Q42 - Q_10 + Q92)
        p2[2] = Q70 + Q71 - Q_10 + Q110 - Q_5 + Q111
        p2[3] = (Q72 - Q_5 + Q112)
        S_p2 = -1000
        p02 = 0
            
        for i in range(4):
            S_temp2 = p2[i]
            if S_temp2 >= S_p2:
                p02 = i
                S_p2 = S_temp2

        p3 = [0,0,0,0]
        p3[0] = Q130 + Q131 - Q_16 + Q170 + Q171 - Q_11
        p3[1] = (Q132 - Q_11 + Q172)
        p3[2] = Q100 + Q101 + Q150 - Q_16 + Q151 - Q_11
        p3[3] = (Q102 - Q_16 + Q152)
        S_p3 = -1000
        p03 = 0
            
        for i in range(4):
            S_temp3 = p3[i]
            if S_temp3 >= S_p3:
                p03 = i
                S_p3 = S_temp3

        p4 = [0,0,0,0]
        p4[0] = Q210 - Q_22 + Q211 - Q_17 + Q160 + Q161
        p4[1] = (Q212 + Q162 - Q_22)
        p4[2] = Q190 + Q191 - Q_22 + Q230 - Q_17 + Q231
        p4[3] = (Q192 - Q_17 + Q232)
        S_p4 = -1000
        p04 = 0
            
        for i in range(4):
            S_temp4 = p4[i]
            if S_temp4 >= S_p4:
                p04 = i
                S_p4 = S_temp4
            
        if (need_yellow1!=0)and(step==(last_traffic_update1+wait_duration1)):
            traci.trafficlight.setPhase("n1",need_yellow1)
            last_traffic_update1 = step
            wait_duration1 = 1
            need_yellow1 = 0
        if (p01 == 0)and(step==(last_traffic_update1+wait_duration1)):
            traci.trafficlight.setPhase("n1",4)
            last_traffic_update1 = step
            wait_duration1 = 12
            need_yellow1 = 5
        if (p01 == 1)and(step==(last_traffic_update1+wait_duration1)):
            traci.trafficlight.setPhase("n1",6)
            last_traffic_update1
            wait_duration1 = 12
            need_yellow1 = 7
        if (p01 == 2)and(step==(last_traffic_update1+wait_duration1)):
            traci.trafficlight.setPhase("n1",0)
            last_traffic_update1 = step
            wait_duration1 = 12
            need_yellow1 = 1
        if (p01 == 3)and(step==(last_traffic_update1+wait_duration1)):
            traci.trafficlight.setPhase("n1",2)
            last_traffic_update1 = step
            wait_duration1 = 12
            need_yellow1 = 3

        if (need_yellow2!=0)and(step==(last_traffic_update2+wait_duration2)):
            traci.trafficlight.setPhase("n2",need_yellow2)
            last_traffic_update2 = step
            wait_duration2 = 1
            need_yellow2 = 0
        if (p02 == 0)and(step==(last_traffic_update2+wait_duration2)):
            traci.trafficlight.setPhase("n2",4)
            last_traffic_update2 = step
            wait_duration2 = 12
            need_yellow2 = 5
        if (p02 == 1)and(step==(last_traffic_update2+wait_duration2)):
            traci.trafficlight.setPhase("n2",6)
            last_traffic_update2 = step
            wait_duration2 = 12
            need_yellow2 = 7
        if (p02 == 2)and(step==(last_traffic_update2+wait_duration2)):
            traci.trafficlight.setPhase("n2",0)
            last_traffic_update2 = step
            wait_duration2 = 12
            need_yellow2 = 1
        if (p02 == 3)and(step==(last_traffic_update2+wait_duration2)):
            traci.trafficlight.setPhase("n2",2)
            last_traffic_update2 = step
            wait_duration2 = 12
            need_yellow2 = 3

        if (need_yellow3!=0)and(step==(last_traffic_update3+wait_duration3)):
            traci.trafficlight.setPhase("n3",need_yellow3)
            last_traffic_update3 = step
            wait_duration3 = 1
            need_yellow3 = 0
        if (p03 == 0)and(step==(last_traffic_update3+wait_duration3)):
            traci.trafficlight.setPhase("n3",4)
            last_traffic_update3 = step
            wait_duration3 = 12
            need_yellow3 = 5
        if (p03 == 1)and(step==(last_traffic_update3+wait_duration3)):
            traci.trafficlight.setPhase("n3",6)
            last_traffic_update3 = step
            wait_duration3 = 12
            need_yellow3 = 7
        if (p03 == 2)and(step==(last_traffic_update3+wait_duration3)):
            traci.trafficlight.setPhase("n3",0)
            last_traffic_update3 = step
            wait_duration3 = 12
            need_yellow3 = 1
        if (p03 == 3)and(step==(last_traffic_update3+wait_duration3)):
            traci.trafficlight.setPhase("n3",2)
            last_traffic_update3 = step
            wait_duration3 = 12
            need_yellow3 = 3

        if (need_yellow4!=0)and(step==(last_traffic_update4+wait_duration4)):
            traci.trafficlight.setPhase("n4",need_yellow4)
            last_traffic_update4 = step
            wait_duration4 = 1
            need_yellow4 = 0
        if (p04 == 0)and(step==(last_traffic_update4+wait_duration4)):
            traci.trafficlight.setPhase("n4",4)
            last_traffic_update4 = step
            wait_duration4 = 12
            need_yellow4 = 5
        if (p04 == 1)and(step==(last_traffic_update4+wait_duration4)):
            traci.trafficlight.setPhase("n4",6)
            last_traffic_update4 = step
            wait_duration4 = 12
            need_yellow4 = 7
        if (p04 == 2)and(step==(last_traffic_update4+wait_duration4)):
            traci.trafficlight.setPhase("n4",0)
            last_traffic_update4 = step
            wait_duration4 = 12
            need_yellow4 = 1
        if (p04 == 3)and(step==(last_traffic_update4+wait_duration4)):
            traci.trafficlight.setPhase("n4",2)
            last_traffic_update4 = step
            wait_duration4 = 12
            need_yellow4 = 3

        step = step + 1
        
    return step,q10,q11,q12,q30,q31,q32,q40,q41,q42,q50,q51,q52,q70,q71,q72,q90,q91,q92,q100,q101,q102,q110,q111,q112,q130,q131,q132,q150,q151,q152,q160,q161,q162,q170,q171,q172,q190,q191,q192,q210,q211,q212,q220,q221,q222,q230,q231,q232,jl10,jl11,jl12,jl30,jl31,jl32,jl40,jl41,jl42,jl50,jl51,jl52,jl70,jl71,jl72,jl90,jl91,jl92,jl100,jl101,jl102,jl110,jl111,jl112,jl130,jl131,jl132,jl150,jl151,jl152,jl160,jl161,jl162,jl170,jl171,jl172,jl190,jl191,jl192,jl210,jl211,jl212,jl220,jl221,jl222,jl230,jl231,jl232,ms10,ms11,ms12,ms30,ms31,ms32,ms40,ms41,ms42,ms50,ms51,ms52,ms70,ms71,ms72,ms90,ms91,ms92,ms100,ms101,ms102,ms110,ms111,ms112,ms130,ms131,ms132,ms150,ms151,ms152,ms160,ms161,ms162,ms170,ms171,ms172,ms190,ms191,ms192,ms210,ms211,ms212,ms220,ms221,ms222,ms230,ms231,ms232
    
    traci.close()
    sys.stdout.flush()

if __name__=="__main__":
    
    options=get_options()
    
    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    traci.start([sumoBinary, "-c", "multi_junction.sumocfg", "--tripinfo-output","tripinfo1.xml"])
    step,q10,q11,q12,q30,q31,q32,q40,q41,q42,q50,q51,q52,q70,q71,q72,q90,q91,q92,q100,q101,q102,q110,q111,q112,q130,q131,q132,q150,q151,q152,q160,q161,q162,q170,q171,q172,q190,q191,q192,q210,q211,q212,q220,q221,q222,q230,q231,q232,jl10,jl11,jl12,jl30,jl31,jl32,jl40,jl41,jl42,jl50,jl51,jl52,jl70,jl71,jl72,jl90,jl91,jl92,jl100,jl101,jl102,jl110,jl111,jl112,jl130,jl131,jl132,jl150,jl151,jl152,jl160,jl161,jl162,jl170,jl171,jl172,jl190,jl191,jl192,jl210,jl211,jl212,jl220,jl221,jl222,jl230,jl231,jl232,ms10,ms11,ms12,ms30,ms31,ms32,ms40,ms41,ms42,ms50,ms51,ms52,ms70,ms71,ms72,ms90,ms91,ms92,ms100,ms101,ms102,ms110,ms111,ms112,ms130,ms131,ms132,ms150,ms151,ms152,ms160,ms161,ms162,ms170,ms171,ms172,ms190,ms191,ms192,ms210,ms211,ms212,ms220,ms221,ms222,ms230,ms231,ms232 = run()
    x = []
    for i in range(step):
        if i%50==0:
            x.append(i)
    plt.plot(x,q10,label="q10")
    plt.plot(x,q11,label="q11")
    plt.plot(x,q12,label="q12")
    plt.plot(x,q30,label="q30")
    plt.plot(x,q31,label="q31")
    plt.plot(x,q32,label="q32")
    plt.plot(x,q40,label="q40")
    plt.plot(x,q40,label="q41")
    plt.plot(x,q42,label="q42")
    plt.plot(x,q50,label="q50")
    plt.plot(x,q51,label="q51")
    plt.plot(x,q52,label="q52")
    plt.plot(x,q70,label="q70")
    plt.plot(x,q71,label="q71")
    plt.plot(x,q72,label="q72")
    plt.plot(x,q90,label="q90")
    plt.plot(x,q91,label="q91")
    plt.plot(x,q92,label="q92")
    plt.plot(x,q100,label="q100")
    plt.plot(x,q101,label="q101")
    plt.plot(x,q102,label="q102")
    plt.plot(x,q110,label="q110")
    plt.plot(x,q111,label="q111")
    plt.plot(x,q112,label="q112")
    plt.plot(x,q130,label="q130")
    plt.plot(x,q131,label="q131")
    plt.plot(x,q132,label="q132")
    plt.plot(x,q150,label="q150")
    plt.plot(x,q151,label="q151")
    plt.plot(x,q152,label="q152")
    plt.plot(x,q160,label="q160")
    plt.plot(x,q161,label="q161")
    plt.plot(x,q162,label="q162")
    plt.plot(x,q170,label="q170")
    plt.plot(x,q171,label="q171")
    plt.plot(x,q172,label="q172")
    plt.plot(x,q190,label="q190")
    plt.plot(x,q191,label="q191")
    plt.plot(x,q192,label="q192")
    plt.plot(x,q210,label="q210")
    plt.plot(x,q211,label="q211")
    plt.plot(x,q211,label="q212")
    plt.plot(x,q220,label="q220")
    plt.plot(x,q221,label="q221")
    plt.plot(x,q222,label="q222")
    plt.plot(x,q230,label="q230")
    plt.plot(x,q231,label="q231")
    plt.plot(x,q232,label="q232")
    plt.xlabel("Time step")
    plt.ylabel("Queue Length")
    plt.title("Queue Length vs Time Steps Backpressure")
    #plt.legend()
    plt.show()
    plt.plot(x,jl10,label="jl10")
    plt.plot(x,jl11,label="jl11")
    plt.plot(x,jl12,label="jl12")
    plt.plot(x,jl30,label="jl30")
    plt.plot(x,jl31,label="jl31")
    plt.plot(x,jl32,label="jl32")
    plt.plot(x,jl40,label="jl40")
    plt.plot(x,jl40,label="jl41")
    plt.plot(x,jl42,label="jl42")
    plt.plot(x,jl50,label="jl50")
    plt.plot(x,jl51,label="jl51")
    plt.plot(x,jl52,label="jl52")
    plt.plot(x,jl70,label="jl70")
    plt.plot(x,jl71,label="jl71")
    plt.plot(x,jl72,label="jl72")
    plt.plot(x,jl90,label="jl90")
    plt.plot(x,jl91,label="jl91")
    plt.plot(x,jl92,label="jl92")
    plt.plot(x,jl100,label="jl100")
    plt.plot(x,jl101,label="jl101")
    plt.plot(x,jl102,label="jl102")
    plt.plot(x,jl110,label="jl110")
    plt.plot(x,jl111,label="jl111")
    plt.plot(x,jl112,label="jl112")
    plt.plot(x,jl130,label="jl130")
    plt.plot(x,jl131,label="jl131")
    plt.plot(x,jl132,label="jl132")
    plt.plot(x,jl150,label="jl150")
    plt.plot(x,jl151,label="jl151")
    plt.plot(x,jl152,label="jl152")
    plt.plot(x,jl160,label="jl160")
    plt.plot(x,jl161,label="jl161")
    plt.plot(x,jl162,label="jl162")
    plt.plot(x,jl170,label="jl170")
    plt.plot(x,jl171,label="jl171")
    plt.plot(x,jl172,label="jl172")
    plt.plot(x,jl190,label="jl190")
    plt.plot(x,jl191,label="jl191")
    plt.plot(x,jl192,label="jl192")
    plt.plot(x,jl210,label="jl210")
    plt.plot(x,jl211,label="jl211")
    plt.plot(x,jl211,label="jl212")
    plt.plot(x,jl220,label="jl220")
    plt.plot(x,jl221,label="jl221")
    plt.plot(x,jl222,label="jl222")
    plt.plot(x,jl230,label="jl230")
    plt.plot(x,jl231,label="jl231")
    plt.plot(x,jl232,label="jl232")
    plt.xlabel("Time step")
    plt.ylabel("Jam Length in meters")
    plt.title("Jam Length vs Time Steps Backpressure")
    #plt.legend()
    plt.show()
    plt.plot(x,ms10,label="ms10")
    plt.plot(x,ms11,label="ms11")
    plt.plot(x,ms12,label="ms12")
    plt.plot(x,ms30,label="ms30")
    plt.plot(x,ms31,label="ms31")
    plt.plot(x,ms32,label="ms32")
    plt.plot(x,ms40,label="ms40")
    plt.plot(x,ms40,label="ms41")
    plt.plot(x,ms42,label="ms42")
    plt.plot(x,ms50,label="ms50")
    plt.plot(x,ms51,label="ms51")
    plt.plot(x,ms52,label="ms52")
    plt.plot(x,ms70,label="ms70")
    plt.plot(x,ms71,label="ms71")
    plt.plot(x,ms72,label="ms72")
    plt.plot(x,ms90,label="ms90")
    plt.plot(x,ms91,label="ms91")
    plt.plot(x,ms92,label="ms92")
    plt.plot(x,ms100,label="ms100")
    plt.plot(x,ms101,label="ms101")
    plt.plot(x,ms102,label="ms102")
    plt.plot(x,ms110,label="ms110")
    plt.plot(x,ms111,label="ms111")
    plt.plot(x,ms112,label="ms112")
    plt.plot(x,ms130,label="ms130")
    plt.plot(x,ms131,label="ms131")
    plt.plot(x,ms132,label="ms132")
    plt.plot(x,ms150,label="ms150")
    plt.plot(x,ms151,label="ms151")
    plt.plot(x,ms152,label="ms152")
    plt.plot(x,ms160,label="ms160")
    plt.plot(x,ms161,label="ms161")
    plt.plot(x,ms162,label="ms162")
    plt.plot(x,ms170,label="ms170")
    plt.plot(x,ms171,label="ms171")
    plt.plot(x,ms172,label="ms172")
    plt.plot(x,ms190,label="ms190")
    plt.plot(x,ms191,label="ms191")
    plt.plot(x,ms192,label="ms192")
    plt.plot(x,ms210,label="ms210")
    plt.plot(x,ms211,label="ms211")
    plt.plot(x,ms211,label="ms212")
    plt.plot(x,ms220,label="ms220")
    plt.plot(x,ms221,label="ms221")
    plt.plot(x,ms222,label="ms222")
    plt.plot(x,ms230,label="ms230")
    plt.plot(x,ms231,label="ms231")
    plt.plot(x,ms232,label="ms232")
    plt.xlabel("Time step")
    plt.ylabel("Mean Speed in meters/sec")
    plt.title("Mean Speed vs Time Steps Backpressure")
    #plt.legend()
    plt.show()

    # Averages
    x1 = []
    ql = []
    for i in range(48):
        x1.append(i)
    ql.append(mean(q10)) 
    ql.append(mean(q11))
    ql.append(mean(q12))
    ql.append(mean(q30))
    ql.append(mean(q31))
    ql.append(mean(q32)) 
    ql.append(mean(q40))
    ql.append(mean(q41))
    ql.append(mean(q42))
    ql.append(mean(q50)) 
    ql.append(mean(q51)) 
    ql.append(mean(q52))
    ql.append(mean(q70))
    ql.append(mean(q71)) 
    ql.append(mean(q72))
    ql.append(mean(q90)) 
    ql.append(mean(q91)) 
    ql.append(mean(q92)) 
    ql.append(mean(q100)) 
    ql.append(mean(q101)) 
    ql.append(mean(q102))
    ql.append(mean(q110)) 
    ql.append(mean(q111)) 
    ql.append(mean(q112)) 
    ql.append(mean(q130)) 
    ql.append(mean(q131))
    ql.append(mean(q132)) 
    ql.append(mean(q150)) 
    ql.append(mean(q151)) 
    ql.append(mean(q152)) 
    ql.append(mean(q160)) 
    ql.append(mean(q161)) 
    ql.append(mean(q162)) 
    ql.append(mean(q170)) 
    ql.append(mean(q171)) 
    ql.append(mean(q172)) 
    ql.append(mean(q190)) 
    ql.append(mean(q191)) 
    ql.append(mean(q192)) 
    ql.append(mean(q210)) 
    ql.append(mean(q211)) 
    ql.append(mean(q212)) 
    ql.append(mean(q220)) 
    ql.append(mean(q221)) 
    ql.append(mean(q222)) 
    ql.append(mean(q230)) 
    ql.append(mean(q231)) 
    ql.append(mean(q232)) 
    plt.plot(x1,ql)
    plt.xlabel("Lanes")
    plt.ylabel("Average Q length")
    plt.title("Average Q length vs Lanes")
    plt.show()
    


            