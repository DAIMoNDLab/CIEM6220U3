#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.dev/sumo
# Copyright (C) 2008-2025 German Aerospace Center (DLR) and others.
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# https://www.eclipse.org/legal/epl-2.0/
# This Source Code may also be made available under the following Secondary
# Licenses when the conditions for such availability set forth in the Eclipse
# Public License 2.0 are satisfied: GNU General Public License, version 2
# or later which is available at
# https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html
# SPDX-License-Identifier: EPL-2.0 OR GPL-2.0-or-later

# @file    runner.py
# @author  Michael Behrisch
# @author  Jakob Erdmann
# @author  Daniel Krajzewicz
# @date    2011-03-04


from __future__ import print_function
from __future__ import absolute_import
import os
import sys
from dotenv import load_dotenv
load_dotenv()

if "SUMO_HOME" in os.environ:
    sys.path.append(os.path.join(os.environ['SUMO_HOME'], 'tools'))

from tud_sumo.simulation import Simulation
from tud_sumo.videos import Recorder
from tud_sumo.plot import Plotter

import simpla  # noqa
from simpla import SimplaException  # noqa

doRecord = False

my_sim = Simulation(scenario_name="Simpla", scenario_desc="Platooning testing")

my_sim.start("sumo.sumocfg", get_individual_vehicle_data=False, gui=True, units="metric")

my_sim.add_tracked_edges()

simpla.load("simpla.cfg.xml")

recorder=Recorder(my_sim)


n, sim_dur, warmup = 1, 250 / my_sim.step_length, 0 / my_sim.step_length

if warmup > 0:
    my_sim.step_through(n_steps=warmup, pbar_max_steps=sim_dur+warmup, keep_data=False)

while my_sim.curr_step < sim_dur + warmup:
    my_sim.step_through(n_seconds=n, pbar_max_steps=sim_dur+warmup)
    if my_sim.curr_step == 2 and doRecord:
        recorder.record_network(recording_name="r1",bounds=((0, 0), (200, 200)),speed=20)
    if my_sim.curr_step >= sim_dur and doRecord:
        recorder.save_recording("r1","platooning_vid.mp4")

plt=Plotter(my_sim,time_unit="minutes")
plt.plot_trajectories(["B999B1000","B999B1000.327"])



