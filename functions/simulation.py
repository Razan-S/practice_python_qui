import os, sys

def check_environment():
    if 'SUMO_HOME' in os.environ:
        tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
        sys.path.append(tools)

        return True
    else:
        sys.exit("Please declare environment variable 'SUMO_HOME'")
        return False
    
def run_simulation():
    try:
        init_position()

        while traci.simulation.getMinExpectedNumber():
            traci.simulationStep()
            
            for intersection in traci.trafficlight.getIDList():
                print("Intersection ID: ", intersection)
                print("Control link: ", traci.trafficlight.getControlledLinks(intersection))

                get_current_light_state(intersection)
                get_time_tls(intersection)

            # tls_pd.produce(state)

    except traci.exceptions.FatalTraCIError:
        end()
        raise HTTPException(status_code=500, detail="SUMO simulation error")
    finally:
        print("Simulation ended")
        end()
        sys.exit(0)

def init_position():
    try:
        x,y = traci.gui.getOffset(viewID=traci.gui.DEFAULT_VIEW)
        zoom = traci.gui.getZoom(viewID=traci.gui.DEFAULT_VIEW)

        position.set_default_position(x, y, zoom)

    except traci.exceptions as e:
        end()
        raise HTTPException(status_code=500, detail="Failed to get position")
    
def end():
    try:
        traci.close()
    except Exception as e:
        process_status.set_stopped()
        process_status.set_disconnected()
        sumo.end()
    finally:
        sys.exit(0)