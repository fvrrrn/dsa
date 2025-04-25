using System.Collections.Generic;

namespace ConsoleApp1
{
    public class RoadMap
    {
        public Town[] towns;
        public List<Road> roads;
        public RoadMap(int n, int m)
        {
            towns = new Town[n];
            for (int i = 0; i < towns.Length; i++)
            {
                towns[i] = new Town();
            }
            roads = new List<Road>(m);
            for (int i = 0; i < roads.Count; i++)
            {
                roads[i] = new Road();
            }
        }

        public void AddRoad(int departureIndex, int arrivalIndex)
        {
            roads.Add(new Road(departureIndex, arrivalIndex));
        }

        public void SetTownCost(int index, int cost)
        {
            towns[index].Cost = cost;
        }

        public int TryReach()
        {
            return TryReach(0, 0);
        }

        private int TryReach(int townIndex, int avgCost)
        {
            if (townIndex == towns.Length - 1) return avgCost;
            
            foreach (var road in roads)
            {
                if (road.DepartureIndex == townIndex)
                {
                    avgCost += towns[townIndex].Cost;
                    int tmp = TryReach(road.ArrivalIndex, avgCost);
                    avgCost = avgCost >= tmp ? tmp : avgCost;
                }
            }
            return avgCost;
        }
    }
}
