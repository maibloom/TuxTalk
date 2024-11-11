#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <curl/curl.h>
#include <webview.h>
#ifdef _WIN32
#include <windows.h>  // For screen dimensions on Windows
#else
#include <X11/Xlib.h> // For screen dimensions on Linux
#endif

// URL to open
const char *url = "https://duckduckgo.com/?q=DuckDuckGo+AI+Chat&ia=chat&duckai=1";

// Structure to hold response data for libcurl
struct MemoryStruct {
    char *memory;
    size_t size;
};

// Callback function for libcurl to write data
static size_t WriteMemoryCallback(void *contents, size_t size, size_t nmemb, void *userp) {
    size_t realsize = size * nmemb;
    struct MemoryStruct *mem = (struct MemoryStruct *)userp;

    char *ptr = realloc(mem->memory, mem->size + realsize + 1);
    if (ptr == NULL) {
        printf("Not enough memory\n");
        return 0;
    }

    mem->memory = ptr;
    memcpy(&(mem->memory[mem->size]), contents, realsize);
    mem->size += realsize;
    mem->memory[mem->size] = 0;

    return realsize;
}

// Function to fetch HTML content from a URL
char *fetch_html(const char *url) {
    CURL *curl_handle;
    CURLcode res;

    struct MemoryStruct chunk;
    chunk.memory = malloc(1);  // Initial memory allocation
    chunk.size = 0;            // Initial size

    curl_global_init(CURL_GLOBAL_ALL);
    curl_handle = curl_easy_init();

    curl_easy_setopt(curl_handle, CURLOPT_URL, url);
    curl_easy_setopt(curl_handle, CURLOPT_WRITEFUNCTION, WriteMemoryCallback);
    curl_easy_setopt(curl_handle, CURLOPT_WRITEDATA, (void *)&chunk);

    res = curl_easy_perform(curl_handle);

    if (res != CURLE_OK) {
        fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
        free(chunk.memory);
        return NULL;
    }

    curl_easy_cleanup(curl_handle);
    curl_global_cleanup();

    return chunk.memory;  // Caller is responsible for freeing this memory
}

// Get screen dimensions
void get_screen_dimensions(int *width, int *height) {
#ifdef _WIN32
    *width = GetSystemMetrics(SM_CXSCREEN);
    *height = GetSystemMetrics(SM_CYSCREEN);
#else
    Display *display = XOpenDisplay(NULL);
    if (display) {
        Screen *screen = DefaultScreenOfDisplay(display);
        *width = screen->width;
        *height = screen->height;
        XCloseDisplay(display);
    } else {
        fprintf(stderr, "Unable to open X display\n");
        *width = 800;
        *height = 600;
    }
#endif
}

int main() {
    // Fetch HTML content (optional)
    char *html_content = fetch_html(url);
    if (html_content) {
        printf("HTML content fetched:\n%s\n", html_content);
        free(html_content);
    } else {
        printf("Failed to fetch HTML content.\n");
    }

    // Get screen dimensions
    int screen_width, screen_height;
    get_screen_dimensions(&screen_width, &screen_height);

    // Set window dimensions and position
    int window_width = screen_width / 3;
    int window_height = screen_height;
    int x_position = screen_width - window_width;
    int y_position = 0;

    // Open the URL in a webview window
    struct webview webview_instance = {
        .title = "My Web App",
        .url = url,
        .width = window_width,
        .height = window_height,
        .x = x_position,
        .y = y_position,
        .resizable = 1
    };

    webview_init(&webview_instance);
    webview_run(&webview_instance);
    webview_exit(&webview_instance);

    return 0;
}
