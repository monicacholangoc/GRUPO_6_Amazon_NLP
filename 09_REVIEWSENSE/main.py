import subprocess
import sys
import argparse


def run_api():
    """Lanza la API FastAPI con uvicorn en el puerto 8000."""
    print("🚀 Iniciando API en http://localhost:8000 ...")
    subprocess.run(
        ["uvicorn", "api_app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"],
        check=True
    )


def run_dashboard():
    """Lanza el dashboard Streamlit en el puerto 8501."""
    print("📊 Iniciando Dashboard en http://localhost:8501 ...")
    subprocess.run(
        ["streamlit", "run", "dashboard_app.py",
         "--server.port", "8501",
         "--server.address", "0.0.0.0"],
        check=True
    )


def run_both():
    """Lanza API y dashboard en paralelo."""
    import threading

    print("🔷 ReviewSense — Iniciando todos los servicios...")
    print("   API       → http://localhost:8000")
    print("   Dashboard → http://localhost:8501")
    print("   Presiona Ctrl+C para detener.\n")

    api_thread  = threading.Thread(target=run_api,  daemon=True)
    dash_thread = threading.Thread(target=run_dashboard, daemon=True)

    api_thread.start()
    dash_thread.start()

    try:
        api_thread.join()
        dash_thread.join()
    except KeyboardInterrupt:
        print("\n🛑 Servicios detenidos.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ReviewSense launcher")
    parser.add_argument("--api",  action="store_true", help="Solo lanza la API")
    parser.add_argument("--dash", action="store_true", help="Solo lanza el dashboard")
    args = parser.parse_args()

    if args.api:
        run_api()
    elif args.dash:
        run_dashboard()
    else:
        run_both()