# =================================================================================================
# Copyright 2011 Twitter, Inc.
# -------------------------------------------------------------------------------------------------
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this work except in compliance with the License.
# You may obtain a copy of the License in the LICENSE file, or at:
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =================================================================================================

from twitter.pants.goal.context import Context
from twitter.pants.goal.goal import Goal
from twitter.pants.goal.group import Group
from twitter.pants.goal.phase import Phase
from twitter.pants.targets.pants_target import Pants
from twitter.pants.tasks import Task, TaskError

pants = Pants
goal = Goal
group = Group
phase = Phase

from .build_file_aliases import *
from .build_file_helpers import *
from .config import Config

# TODO(John Sirois): XXX kill
from .build_environment import *
