import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path
import toml
from dtw_lab.lab1 import (
    read_csv_from_google_drive,
    visualize_data,
    calculate_statistic,
    clean_data,
)

app = FastAPI()


def run_server(port: int = 80, reload: bool = False, host: str = "127.0.0.1"):
    uvicorn.run("dtw_lab.lab2:app", port=port, reload=reload, host=host)


@app.get("/")
def main_route():
    return {"message": "Hello world"}


@app.get("/statistic/{measure}/{column}")
def get_statistic(measure: str, column: str):
    df = read_csv_from_google_drive("1eKiAZKbWTnrcGs3bqdhINo1E4rBBpglo")
    df = clean_data(df)
    statistic = calculate_statistic(measure, df[column])
    return {"message": f"The {measure} for column {column} is {statistic}"}


@app.get("/visualize/{graph_type}")
def get_visualization(graph_type: str):
    df = read_csv_from_google_drive("1eKiAZKbWTnrcGs3bqdhINo1E4rBBpglo")
    df = clean_data(df)
    visualize_data(df)
    image_path = Path(f"graphs/{graph_type}.png")
    if not image_path.is_file():
        return {"error": "Image not found on the server"}
    return FileResponse(image_path)

@app.get("/version")
def get_visualization_version():
    pyproject_path = Path(__file__).resolve().parents[2] / "pyproject.toml"
    pyproject_data = toml.load(pyproject_path)
    version = pyproject_data["tool"]["poetry"]["version"]
    return {"version": version}