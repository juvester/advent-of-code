#include <bits/stdc++.h>
#include <iostream>
#include <deque>

using namespace std;

#define ull unsigned long long

size_t N = 20;
size_t inspections[] = {0, 0, 0, 0, 0, 0, 0, 0};

int main()
{
    deque<ull> monkey0{96, 60, 68, 91, 83, 57, 85};
    deque<ull> monkey1{75, 78, 68, 81, 73, 99};
    deque<ull> monkey2{69, 86, 67, 55, 96, 69, 94, 85};
    deque<ull> monkey3{88, 75, 74, 98, 80};
    deque<ull> monkey4{82};
    deque<ull> monkey5{72, 92, 92};
    deque<ull> monkey6{74, 61};
    deque<ull> monkey7{76, 86, 83, 55};

    for (size_t i = 0; i < N; i++)
    {
        while (!monkey0.empty())
        {
            ull item = monkey0[0];
            monkey0.pop_front();
            item *= 2;
            item /= 3;
            if (item % 17 == 0)
                monkey2.push_back(item);
            else
                monkey5.push_back(item);
            inspections[0]++;
        }

        while (!monkey1.empty())
        {
            ull item = monkey1[0];
            monkey1.pop_front();
            item += 3;
            item /= 3;
            if (item % 13 == 0)
                monkey7.push_back(item);
            else
                monkey4.push_back(item);
            inspections[1]++;
        }

        while (!monkey2.empty())
        {
            ull item = monkey2[0];
            monkey2.pop_front();
            item += 6;
            item /= 3;
            if (item % 19 == 0)
                monkey6.push_back(item);
            else
                monkey5.push_back(item);
            inspections[2]++;
        }

        while (!monkey3.empty())
        {
            ull item = monkey3[0];
            monkey3.pop_front();
            item += 5;
            item /= 3;
            if (item % 7 == 0)
                monkey7.push_back(item);
            else
                monkey1.push_back(item);
            inspections[3]++;
        }

        while (!monkey4.empty())
        {
            ull item = monkey4[0];
            monkey4.pop_front();
            item += 8;
            item /= 3;
            if (item % 11 == 0)
                monkey0.push_back(item);
            else
                monkey2.push_back(item);
            inspections[4]++;
        }

        while (!monkey5.empty())
        {
            ull item = monkey5[0];
            monkey5.pop_front();
            item *= 5;
            item /= 3;
            if (item % 3 == 0)
                monkey6.push_back(item);
            else
                monkey3.push_back(item);
            inspections[5]++;
        }

        while (!monkey6.empty())
        {
            ull item = monkey6[0];
            monkey6.pop_front();
            item *= item;
            item /= 3;
            if (item % 2 == 0)
                monkey3.push_back(item);
            else
                monkey1.push_back(item);
            inspections[6]++;
        }

        while (!monkey7.empty())
        {
            ull item = monkey7[0];
            monkey7.pop_front();
            item += 4;
            item /= 3;
            if (item % 5 == 0)
                monkey4.push_back(item);
            else
                monkey0.push_back(item);
            inspections[7]++;
        }
    }

    sort(inspections, inspections + 8);
    ull result = inspections[6] * inspections[7];
    cout << result << endl;
}
