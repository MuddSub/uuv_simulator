# Copyright (c) 2016-2019 The UUV Simulator Authors.
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import rospy
import numpy
from .thruster import Thruster


class ThrusterUnity(Thruster):
    """ Output = Input. No transformations, no nonsense. Used for running
    thruster allocation with the real-world robot.


    > *Input arguments*

    * `index` (*type:* `int`): Thruster's ID.
    * `topic` (*type:* `str`): Thruster's command topic.
    * `pos` (*type:* `numpy.array` or `list`): Position vector
    of the thruster with respect to the vehicle's frame.
    * `orientation` (*type:* `numpy.array` or `list`): Quaternion
    with the orientation of the thruster with respect to the vehicle's
    frame as `(qx, qy, qz, qw)`.
    * `axis` (*type:* `numpy.array`): Axis of rotation of the thruster.
    """
    LABEL = 'unity'

    def __init__(self, *args, **kwargs):
        super(ThrusterUnity, self).__init__(*args)

        if 'gain' not in kwargs:
            rospy.ROSException('Thruster gain not given')
        rospy.loginfo('Thruster model: Unity')

    def get_command_value(self, thrust):
        """Compute the angular velocity necessary
        for the desired thrust force.

        > *Input arguments*

        * `thrust` (*type:* `float`): Thrust force magnitude in N

        > *Returns*

        `float`: Angular velocity set-point for the thruster in rad/s
        """
        return thrust

    def get_thrust_value(self, command):
        """Computes the thrust force for the given angular velocity
        set-point.

        > *Input arguments*

        * `command` (*type:* `float`): Angular velocity set-point for
        the thruster in rad/s

        > *Returns*

        `thrust` (*type:* `float`): Thrust force magnitude in N
        """
        return command
