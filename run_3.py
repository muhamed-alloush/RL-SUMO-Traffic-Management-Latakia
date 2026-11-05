import traci
import pickle

# ======================
# تحميل الموديلات
# ======================
agents = {}

junctions = [
    "10690046828",
    "2150474538",
    "968598847",
    "968598852",
    "cluster_10674700244_968598851",
    "cluster_2073166363_968593314"
]

for j in junctions:
    with open(f"q_table_{j}.pkl", "rb") as f:
        agents[j] = pickle.load(f)

print("✅ Loaded all models")

# ======================
# STATE
# ======================
def get_state(junction):
    lanes = traci.trafficlight.getControlledLanes(junction)
    state = []

    for lane in lanes:
        cars = traci.lane.getLastStepHaltingNumber(lane)
        state.append(min(cars, 5))

    return tuple(state)

# ======================
# اختيار action الصحيح
# ======================
def choose_action(Q, state, junction):
    logic = traci.trafficlight.getAllProgramLogics(junction)[0]
    num_phases = len(logic.phases)

    return max(range(num_phases), key=lambda a: Q.get((state, a), 0.0))

# ======================
# تشغيل SUMO
# ======================
traci.start(["sumo-gui", "-c", "osm.sumocfg", "--scale", "3"])

step = 0
phase_duration = 10
counter = 0

while step < 5000:

    if counter == 0:
        for j in junctions:
            state = get_state(j)
            action = choose_action(agents[j], state, j)
            traci.trafficlight.setPhase(j, action)

    traci.simulationStep()

    step += 1
    counter += 1

    if counter >= phase_duration:
        counter = 0

traci.close()
print("✅ Simulation finished")