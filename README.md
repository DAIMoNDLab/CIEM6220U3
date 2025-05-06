# CIEM6220U3
## 2025 Intelligent Vehicles Control/Platooning simulation

- This simulation is based on DRL SUMO, please make sure this is installed in your system before continuing
- We recommend employing .conda environments where feasible (we recommend miniconda)
- This software was last tested with Python 3.11.


### Quick install guide:
- Create a local clone of this repository
- Open the repository as a folder in VSCode (or, other IDE of your choice)
- Create a .conda environment within the local repository copy folder, activate it
- Using pip, install the following packages: "dotenv", "tud-sumo"
    - pip install dotenv
    - pip install tud-sumo

### Quick use guide:
The simulation is launched by running 'tudsumo-runner.py'.
Changes in the configuration of the simulation must be made manually in the appropriate input file:
- behavioural changes (e.g. which vehicle model is used, or what is the desired time gap $\tau$, or demand) can be implemented in 'input_routes.rou.xml'; for example:
    - <vType id="lorry" vClass="truck" color="orange" maxSpeed="5"/> -> a lorry with a max speed of 18km/h
    - <vType id="t_follower" color="green" minGap="0.5" tau="1.3" carFollowModel="CACC"/> -> platoon follower vehicles use the CACC car following model, with a desired time gap of 1.3s
    - <flow id="v" type="car" begin="0" number="8" period="2" departSpeed="max" from="B999B1000" to="B999B1000.327" /> -> the platoon consists of a total of eight (8) vehicles, all entering at time 0 every 2 time steps
    - <flow id="lr" type="lorry" begin="25" number="1" period="2" departSpeed="max" from="B999B1000" to="B999B1000.327" /> -> a (slow) lorry enters the network at time 25

 By changing these parameters you can try different values and assess.

