from graspit_commander import GraspitCommander

import time

if __name__ == "__main__":
    GraspitCommander.clearWorld()
    GraspitCommander.loadWorld("plannerMug")

    GraspitCommander.approachToContact()

    GraspitCommander.setDynamics(True)
    GraspitCommander.setDynamics(False)
    GraspitCommander.toggleDynamicsController(False)
    
    while not GraspitCommander.dynamicAutoGraspComplete():
        r = GraspitCommander.getRobot(0)
        print r.robot.dofs
        GraspitCommander.setRobotDOFForces([0, 100000000, 100000000, 100000000])
        GraspitCommander.stepDynamics(1)


    r = GraspitCommander.getRobot(0)
    dofs = list(r.robot.dofs)

    for i in range(len(dofs)):
        dofs[i] -= 0.01

    GraspitCommander.toggleAllCollisions(False)
    GraspitCommander.autoOpen(0)
    GraspitCommander.approachToContact(-10)
    GraspitCommander.toggleAllCollisions(True)
    GraspitCommander.approachToContact(10)

    GraspitCommander.forceRobotDof(dofs)
    GraspitCommander.autoGrasp(0)

    graspQuality = GraspitCommander.computeQuality()
    print "DONE!"
    print graspQuality.epsilon
    print graspQuality.volume

