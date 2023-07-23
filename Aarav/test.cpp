#include <iostream>
#include <vector>
using namespace std;

class Observer {
public:
    virtual void notify() = 0; // pure virtual function
};
class EventSource {
private:
    vector<Observer*> observers;
public:
    void addObserver(Observer* observer) {
        observers.push_back(observer);
    }
    void triggerEvent() {
        for (Observer* observer : observers) {
            observer->notify();
        }
    }
};
class ObserverImpl : public Observer {
public:
    void notify() override {
        cout << "An event has occurred!" << endl;
    }
};
int main() {
    EventSource eventSource;
    ObserverImpl observer;

    eventSource.addObserver(&observer);
    eventSource.triggerEvent(); // outputs: An event has occurred!

    return 0;
}
