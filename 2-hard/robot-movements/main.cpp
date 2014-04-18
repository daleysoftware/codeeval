#include <iostream>

int countPaths(bool grid[][4], int currentX, int currentY)
{
    if (currentX < 0 || currentX > 3 || currentY < 0 || currentY > 3) {
        return 0;
    }

    if (grid[currentX][currentY]) {
        return 0;
    }

    if (currentX == 3 && currentY == 3) {
        return 1;
    }

    grid[currentX][currentY] = true;

    int result = 0;

    result += countPaths(grid, currentX+1, currentY);
    result += countPaths(grid, currentX,   currentY+1);
    result += countPaths(grid, currentX-1, currentY);
    result += countPaths(grid, currentX,   currentY-1);

    grid[currentX][currentY] = false;

    return result;
}

int main()
{
    bool grid[][4] = {
        {false, false, false, false},
        {false, false, false, false},
        {false, false, false, false},
        {false, false, false, false}
    };

    std::cout << countPaths(grid, 0, 0) << std::endl;
    return 0;
}
