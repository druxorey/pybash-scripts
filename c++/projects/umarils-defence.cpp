#include <iostream>
#include <cmath>

using namespace std;

float gravityAcceleration = 9.81;
float errorRange = 1.6;

int roundUp(float number) {
    int decimal = (number - (int)number) * 10;
    if (decimal >= 5) {return number + 1;} 
    else {return number;}
}


float degreeToRadians(float degrees) {
    return degrees * M_PI / 180;
}


float radiansToDegrees(float radians) {
    return radians * 180/ M_PI;
}


float distanceDifference(float target, int cannon) {
    return target - cannon;
}


int maxHeight(float velocity, float degrees, float cannon) {
    float radians = degreeToRadians(degrees);
    float height = ((velocity * velocity * sin(radians) * sin(radians)) / (2 * gravityAcceleration)) + cannon;
    return roundUp(height);
} 


int maxTime(float velocity, float degrees) {
    if (degrees == 90) {
        return roundUp(velocity / gravityAcceleration);
    } else {
        float radians = degreeToRadians(degrees);
        float time = (2 * velocity * sin(radians)) / gravityAcceleration;
        return roundUp(time);
    }
}


float calculateXVelocity(int velocity, float degrees) {
    return velocity * cos(degreeToRadians(degrees));
}

 
float calculateYVelocity(int velocity, float degrees) {
    return velocity * sin(degreeToRadians(degrees));
}


int calculateImpactTime(float velocity, float distance) {
    return distance / velocity;
}


int calculateVerticalImpactTime(int velocity, int height){
    float discriminant = (pow(velocity, 2)) - (2 * gravityAcceleration * height);
    return (velocity - sqrt(discriminant)) / gravityAcceleration;
}


float calculateXPosition(int velocity, float impactTime, float degrees) {
    return velocity * impactTime * cos(degreeToRadians(degrees));
}


float calculateYPosition(float cannonPosition, float velocity, int impactTime){
    return cannonPosition + velocity * impactTime - (0.5 * gravityAcceleration * (impactTime * impactTime));
}


int calculateAngleAdjustment(float angle, int degrees) {
    int finalAngle = (degrees > 90)? 180 - degrees : degrees;
    return roundUp(abs(radiansToDegrees(angle) - finalAngle));
}


int main(){
    int cannonsQuantity, xCannonPosition, yCannonPosition, targetNumber, initialVelocity, degreesShootingAngle;
    float xTargetPosition, yTargetPosition;
    bool isCannonsValid = false;

    printf("Ingresa la cantidad de cañones a simular: ");
    cin >> cannonsQuantity;

    while(cannonsQuantity < 1 || cannonsQuantity > 26){
        cin.clear(); 
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        printf("!Número de cañones inválido!\nIngresa la cantidad de cañones a simular: ");
        cin >> cannonsQuantity;
    }

    for (int cannon = 1; cannon <= cannonsQuantity; cannon++) {
        bool isCannonDead = false;
        int target = 1;
        char displayedCannon = cannon + 64;

        printf("\nIngresa la posición del cañón %c [x y]: ",displayedCannon);
        cin >> xCannonPosition;
        cin >> yCannonPosition;
        printf("Ingresa la velocidad inicial del proyectil: ");
        cin >> initialVelocity;
        printf("Ingresa el ángulo de disparo: ");
        cin >> degreesShootingAngle;
        printf("Ingresa el número de objetivos: ");
        cin >> targetNumber;

        if (yCannonPosition < 0 || yCannonPosition > 50 ||
            initialVelocity < 1 || initialVelocity > 500 ||
            degreesShootingAngle < 0 || degreesShootingAngle > 180 ||
            targetNumber < 1) {
            printf("Datos de entrada inválidos...\n");
            return 0;
        }  

        int maxHeightValue = maxHeight(initialVelocity, degreesShootingAngle, yCannonPosition);
        printf("\nLos proyectiles del cañón %c subirán hasta %i metros antes de caer.\n", displayedCannon, maxHeightValue);

        int maxTimeValue = maxTime(initialVelocity, degreesShootingAngle);
        printf("Estos impactaran contra el suelo pasados %i segundos luego de ser disparados.\n", maxTimeValue);

        do {
            printf("\nIngresa la posición del objetivo %i [x y]: ",target);
            cin >> xTargetPosition;
            cin >> yTargetPosition;

            if (yTargetPosition < 0) {printf("Datos de entrada inválidos...\n"); return 0;}

            float xInitialVelocity = calculateXVelocity(initialVelocity, degreesShootingAngle);
            float yInitialVelocity = calculateYVelocity(initialVelocity, degreesShootingAngle);

            float xDistanceDifference = distanceDifference(xTargetPosition, xCannonPosition);
            float yDistanceDifference = distanceDifference(yTargetPosition, yCannonPosition);

            int impactTime = calculateImpactTime(xInitialVelocity, xDistanceDifference);

            float xProjectilePosition = calculateXPosition(initialVelocity, impactTime, degreesShootingAngle);
            float yProjectilePosition = calculateYPosition(yCannonPosition, yInitialVelocity, impactTime);

            if ((xCannonPosition == xTargetPosition) && (yCannonPosition == yTargetPosition)) {
                printf("Cañón destruído\n");
                isCannonDead = true;

            } else if ((xCannonPosition == xTargetPosition) && (yCannonPosition > yTargetPosition)) {
                printf("Enemigo en las Murallas\n");

            } else if ((xCannonPosition > xTargetPosition && degreesShootingAngle < 90) || xCannonPosition < xTargetPosition && degreesShootingAngle > 90) {
                printf("Posición comprometida\n");

            } else if ((abs(xProjectilePosition - xTargetPosition) < errorRange) && (abs(yProjectilePosition - yTargetPosition) < errorRange)) {
                printf("Objetivo %i destruído por el cañón %c en %i segundos.\n", target, displayedCannon, impactTime);

            } else if (yTargetPosition > yCannonPosition && xTargetPosition == xCannonPosition && degreesShootingAngle == 90) {
                int impactTime = calculateVerticalImpactTime(initialVelocity, yTargetPosition);
                printf("Objetivo %i destruído por el cañón %c en %i segundos.\n", target, displayedCannon, impactTime);

            } else {
                float quadraticTerm = ((-1 * gravityAcceleration)*pow(xDistanceDifference,2))/(2*pow(initialVelocity,2));
                float linearTerm = abs(xDistanceDifference);
                float constantTerm = (((-1 * gravityAcceleration)*pow(xDistanceDifference,2))/(2*pow(initialVelocity,2)))-(yDistanceDifference);
                float discriminantValue = (pow(linearTerm, 2)) - (4 * quadraticTerm * constantTerm);

                if (discriminantValue < 0) {
                    printf("El objetivo %i no está en rango de ataque.\n", target);

                } else {
                    float rootValue = sqrt(discriminantValue);
                    float fixedAngle = atan(((-1 * linearTerm) + rootValue) / (2 * quadraticTerm));
                    int angleAdjustment = calculateAngleAdjustment(fixedAngle, degreesShootingAngle);

                    angleAdjustment = (xCannonPosition == xTargetPosition && degreesShootingAngle != 90)? abs(90 - degreesShootingAngle): angleAdjustment;

                    printf("Reajuste de %i grados requerido en el cañón %c.\n", angleAdjustment, displayedCannon);
                }
            }
            target++;

        } while (isCannonDead == false && target <= targetNumber);
    }

    return 0;
}
