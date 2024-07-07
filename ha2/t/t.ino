#include "image_arrays.h"
#include <TFT_eSPI.h> // Make sure to install this library via Library Manager

TFT_eSPI tft; // Initialize TFT display object

void setup() {
    tft.init();
    tft.setRotation(3); // Adjust the rotation according to your display
    tft.fillScreen(TFT_BLACK); // Clear screen
}

void loop() {
    // Display an image (example)
    displayImage(walk, animation_width, animation_height); // Assuming 'walk' is one of the arrays defined in image_arrays.h
    delay(5000); // Display each image for 5 seconds
    tft.fillScreen(TFT_BLACK); // Clear screen after displaying
}

void displayImage(const unsigned short* image, int width, int height) {
    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            tft.drawPixel(x, y, image[y * width + x]);
        }
    }
}
