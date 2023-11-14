float __sacalon__mean(std::vector<int> const& v) {
    float mean = 0.0;
    for (auto x : v) {
        mean += x;
    }
    mean = mean / v.size();
    return mean;
}

float __sacalon__mean(std::vector<float> const& v) {
    float mean = 0.0;
    for (auto x : v) {
        mean += x;
    }
    mean = mean / v.size();
    return mean;
}

double __sacalon__mean(std::vector<double> const& v) {
    double mean = 0.0;
    for (auto x : v) {
        mean += x;
    }
    mean = mean / v.size();
    return mean;
}

double __sacalon__pow(double a,double b){
    return pow(a,b);
}

float __sacalon__round(float arg){
    return std::round(arg);
}

double __sacalon__round(double arg){
    return std::round(arg);
}