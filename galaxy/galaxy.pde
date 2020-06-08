// Original: https://www.reddit.com/r/processing/comments/dswnx6/a_galaxy_in_35_lines_of_code/

ArrayList<PShape> rings = new ArrayList<PShape>();
int ringCount = 50;
void setup(){
    size(640, 480, P3D);
    blendMode(ADD);
    float innerRad = 1f, outerRad = 9f, increment = ringCount/50f;
    for(int ringIndex = 0; ringIndex < ringCount; ringIndex++) {
        PShape ring = createShape();
        ring.setStrokeWeight(1.5f);
        ring.beginShape(POINTS);
        ring.stroke(lerpColor(color(73, 115, 161), color(157, 47, 77), ringIndex/50f), 175f);
        for(int starIndex = 0; starIndex < 3000; starIndex++) {
            float a = random(0f, 1f) * TWO_PI;
            float r = sqrt(random(sq(innerRad), sq(outerRad)));
            ring.vertex(r * cos(a), r * sin(a), random(-increment, increment));
        }
        ring.endShape();
        rings.add(ring);
        innerRad += increment;
        outerRad += increment * 1.5f;
        increment += 1;
    }
}

void draw() {
    background(0);
    camera(-width/2f, -height/2f, 150f, 0f, 0f, 0f, 0f, 1f, 0f);
    for(int index = 0; index < ringCount; index++) {
        pushMatrix();
        rotateY((TWO_PI/(index*index)*frameCount)/10);
        rotateX(1.45f);
        shape(rings.get(index));
        popMatrix();
    }
}
