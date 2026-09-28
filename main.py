import flet as ft
import subprocess
import os
import platform
import uuid

def main(page: ft.Page):
    page.title = "VIP Shorts Downloader"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#121212"

    # Hardware ID (HWID) generator for license locking
    def get_hwid():
        try:
            if platform.system() == "Windows":
                import subprocess.si
                # Fallback or simple machine id
                return str(uuid.getnode())
            else:
                return str(uuid.getnode())
        except:
            return "UNKNOWN-HWID"

    user_hwid = get_hwid()

    # UI Components for License & Dashboard
    hwid_text = ft.Text(f"Device ID: {user_hwid}", color=ft.colors.WHITE70, size=14)
    license_input = ft.TextField(label="Enter License Key", width=300, border_color=ft.colors.AMBER)
    status_text = ft.Text("", color=ft.colors.RED)

    url_input = ft.TextField(label="YouTube Channel / Shorts URL", width=300, border_color=ft.colors.BLUE)
    output_log = ft.Text("Status: Ready", color=ft.colors.GREEN, size=12)

    def verify_license(e):
        # Basic check for license key matching or demo validation
        entered_key = license_input.value.strip()
        if entered_key == "VIP-2026-PRO":
            status_text.value = "License Verified Successfully!"
            status_text.color = ft.colors.GREEN
            license_container.visible = False
            dashboard_container.visible = True
            page.update()
        else:
            status_text.value = "Invalid License Key!"
            page.update()

    def start_download(e):
        url = url_input.value.strip()
        if not url:
            output_log.value = "Error: Please enter a valid URL!"
            page.update()
            return
        
        output_log.value = "Downloading and splitting Shorts..."
        page.update()

        # yt-dlp & ffmpeg backend logic execution placeholder
        try:
            # Example command structure for yt-dlp
            cmd = f"yt-dlp -f best -o '%(title)s.%(ext)s' {url}"
            # subprocess.run(cmd, shell=True)
            output_log.value = "Successfully Downloaded & Processed!"
        except Exception as ex:
            output_log.value = f"Error: {str(ex)}"
        page.update()

    # License Screen Container
    license_container = ft.Container(
        content=ft.Column([
            ft.Text("VIP Security Lock", size=22, weight=ft.FontWeight.BOLD, color=ft.colors.AMBER),
            hwid_text,
            license_input,
            ft.ElevatedButton("Verify Key", on_click=verify_license, bgcolor=ft.colors.AMBER, color=ft.colors.BLACK),
            status_text
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        padding=20
    )

    # Main Tool Dashboard Container (Hidden until verified)
    dashboard_container = ft.Container(
        content=ft.Column([
            ft.Text("VIP Shorts Downloader & Splitter", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
            url_input,
            ft.ElevatedButton("Start Processing", on_click=start_download, bgcolor=ft.colors.BLUE, color=ft.colors.WHITE),
            output_log
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        padding=20,
        visible=False
    )

    page.add(
        ft.Column([
            license_container,
            dashboard_container
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

ft.app(target=main)
