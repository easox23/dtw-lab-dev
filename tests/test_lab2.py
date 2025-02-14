from src.dtw_lab.lab1 import calculate_statistic
from src.dtw_lab.lab2 import get_statistic
import pandas as pd
import pytest


def test_calculate_statistic():
    df = pd.DataFrame({"Charge_Left_Percentage": [39, 60, 30, 30, 41]})
    assert calculate_statistic("mean", df["Charge_Left_Percentage"]) == 40
    assert calculate_statistic("median", df["Charge_Left_Percentage"]) == 39
    assert calculate_statistic("mode", df["Charge_Left_Percentage"]) == 30




def test_get_statistic(mocker):
    # Mock the read_csv_from_google_drive function
    mock_read_csv = mocker.patch("src.dtw_lab.lab2.read_csv_from_google_drive")
    mock_read_csv.return_value = pd.DataFrame(
        {
            "Battery_Size": ["C", "C", "AA", "AAA", "C", "AAA", "D", "AA", "D", "C"],
            "Avg_Operating_Temperature": [
                10.0,
                10.0,
                24.0,
                5.0,
                28.0,
                15.0,
                24.0,
                20.0,
                20.0,
                16.0,
            ],
            "Discharge_Speed": [
                "Slow",
                "Fast",
                "Fast",
                "Slow",
                "Medium",
                "Medium",
                "Medium",
                "Medium",
                "Slow",
                "Fast",
            ],
            "Manufacturer": [
                "EnergyPlus",
                "EnergyPlus",
                "WhiteRabbit",
                "ElectricPower",
                "WhiteRabbit",
                "WhiteRabbit",
                "WhiteRabbit",
                "ElectricPower",
                "WhiteRabbit",
                "EnergyPlus",
            ],
            "Days_Since_Production": [
                343.0,
                932.0,
                439.0,
                833.0,
                246.0,
                603.0,
                160.0,
                786.0,
                659.0,
                896.0,
            ],
            "Nominal_Voltage": [2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0],
            "Voltage_Cutoff": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            "Current_Voltage": [1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            "Serial_Number": [
                "3EE1N56TLH",
                "TD5XHNDA43",
                "F0MS4AO5G0",
                "W33XMN9VFC",
                "2DM8HMYAHN",
                "0VFSH611PB",
                "TA7L8O8K3L",
                "CV4ZAFS0DU",
                "H7NIEX58C6",
                "1AR1E0T4UZ",
            ],
            "Charge_Left_Percentage": [
                60.0,
                28.0,
                28.0,
                None,
                52.0,
                10.0,
                6.0,
                26.0,
                36.0,
                37.0,
            ],
        }
    )


    response = get_statistic("mean", "Charge_Left_Percentage")
    assert response == {"message": "The mean for column Charge_Left_Percentage is 31.875"}

    mock_read_csv.assert_called_once()