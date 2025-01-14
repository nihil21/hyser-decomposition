"""Copyright 2022 Mattia Orlandi

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os

import numpy as np
import wfdb


def load_pr(
    root: str,
    gesture: int,
    subject: int,
    session: int,
    trial: int,
    task: int,
    task_type: str,
    sig_type: str,
) -> np.ndarray:
    """Load data from the 1DoF subset.

    Parameters
    ----------
    root : str
        Path to Hyser dataset root folder.
    gesture : int,
        Gesture id.
    subject : int
        Subject id.
    session : int
        Session id.
    trial : int
        Trial id.
    task : int
        Task id.
    task_type : {"maintenance", "dynamic"}
        Task type.
    sig_type : {"raw", "preprocess", "force"}
        Signal type.

    Returns
    -------
    ndarray
        Array containing the sEMG signal for the given gesture, subject, session, trial and task.
    """

    assert task_type in [
        "maintenance",
        "dynamic",
    ], 'The signal type must be either "maintenance" or "dynamic".'
    assert sig_type in [
        "raw",
        "preprocess",
        "force",
    ], 'The signal type must be either "raw", "preprocess" or "force".'

    path = os.path.join(
        root,
        "pr_dataset",
        f"{gesture:02d}",
        f"subject{subject:02d}_session{session}_{task_type}_{sig_type}_trial{trial}_task{task}",
    )
    data, _ = wfdb.rdsamp(path)

    return data.T


def load_1dof(
    root: str, subject: int, session: int, task: int, trial: int, sig_type: str = "raw"
) -> np.ndarray:
    """Load data from the 1DoF subset.

    Parameters
    ----------
    root : str
        Path to Hyser dataset root folder.
    subject : int
        Subject id.
    session : int
        Session id.
    task : int
        Task id.
    trial : int
        Trial id.
    sig_type : {"raw", "preprocess", "force"}
        Signal type.

    Returns
    -------
    ndarray
        Array containing the sEMG signal for each finger and trial.
    """

    assert sig_type in [
        "raw",
        "preprocess",
        "force",
    ], 'The signal type must be either "raw", "preprocess" or "force".'

    path = os.path.join(
        root,
        "1dof_dataset",
        f"subject{subject:02d}_session{session}",
        f"1dof_{sig_type}_finger{task}_sample{trial}",
    )
    data, _ = wfdb.rdsamp(path)

    return data.T


def load_mvc(
    root: str,
    subject: int,
    session: int,
    task: int,
    direction: str,
    sig_type: str = "raw",
) -> np.ndarray:
    """Load data from the MVC subset.

    Parameters
    ----------
    root : str
        Path to Hyser dataset root folder.
    subject : int
        Subject id.
    session : int
        Session id.
    task : int
        Task id.
    direction : {"extension", "flexion"}
        Direction of the movement.
    sig_type : {"raw", "preprocess", "force"}
        Signal type.

    Returns
    -------
    ndarray
        Dictionary containing the sEMG signal for each finger.
    """

    assert sig_type in [
        "raw",
        "preprocess",
        "force",
    ], 'The signal type must be either "raw", "preprocess" or "force".'

    path = os.path.join(
        root,
        "mvc_dataset",
        f"subject{subject + 1:02d}_session{session + 1}",
        f"mvc_{sig_type}_finger{task}_{direction}",
    )
    data, _ = wfdb.rdsamp(
        os.path.join(
            path,
        )
    )

    return data.T


def load_ndof(
    root: str,
    subject: int,
    session: int,
    combination: int,
    trial: int,
    sig_type: str = "raw",
) -> np.ndarray:
    """Load data from the 1DoF subset.

    Parameters
    ----------
    root : str
        Path to Hyser dataset root folder.
    subject : int
        Subject id.
    session : int
        Session id.
    combination : int
        Combination id.
    trial : int
        Trial id.
    sig_type : {"raw", "preprocess", "force"}
        Signal type.

    Returns
    -------
    ndarray
        Array containing the sEMG signal for each finger and trial.
    """

    assert sig_type in [
        "raw",
        "preprocess",
        "force",
    ], 'The signal type must be either "raw", "preprocess" or "force".'

    path = os.path.join(
        root,
        "ndof_dataset",
        f"subject{subject:02d}_session{session}",
        f"ndof_{sig_type}_combination{combination}_sample{trial}",
    )
    data, _ = wfdb.rdsamp(path)

    return data.T
