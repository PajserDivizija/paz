import numpy as np
from paz.abstract.messages import Box2D, Pose6D
import pytest


@pytest.fixture(params=[[219, 49, 319, 179]])
def box_coordinates(request):
    return (request.param)


@pytest.fixture(params=[60.0, 80.0])
def score(request):
    return request.param


@pytest.fixture
def quaternion():
    _quaternion = np.array([-0.4732069, 0.5253096, 0.4732069, 0.5255476])
    return _quaternion


@pytest.fixture
def translation():
    _translation = np.array([1.0, 0.765, 0])
    return _translation


@pytest.fixture
def rotation_vector():
    vector = np.array([1., -0.994522, 0.104528])
    return vector


@pytest.fixture
def quaternion_result():
    result = np.array([0.45936268, -0.45684629, 0.04801626, 0.76024458])
    return result


@pytest.mark.parametrize("test_point", [[256, 60], [219, 49]])
def test_Box2D(box_coordinates, score, test_point):
    """ Unit test for Bounding box 2D with class
    and score
    """
    box2D = Box2D(box_coordinates, score)
    assert (box2D.contains(test_point))


def test_Pose6D(quaternion, translation, rotation_vector, quaternion_result):
    """Unit test for Pose estimation
    """
    pose6D = Pose6D(quaternion, translation)
    result = pose6D.from_rotation_vector(rotation_vector, translation)
    assert(result.quaternion.all() == quaternion_result.all())
