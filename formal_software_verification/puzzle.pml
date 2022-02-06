bit father = 0;
bit son_1 = 0;
bit son_2 = 0;
bit father_on_board = 0;
bit son_1_on_board = 0;
bit son_2_on_board = 0;
bit boat = 0;
bit on_water = 0;

#define safe ((father_on_board * 200 + son_1_on_board * 100 + son_2_on_board * 100) <= 200 || !on_water)

active proctype main() {
  do
  :: (father_on_board == 0 && father == boat && !on_water) -> atomic { printf("father get on board\n"); father_on_board = 1 }
  :: (son_1_on_board == 0 && son_1 == boat && !on_water)   -> atomic { printf("son_1 get on board\n");  son_1_on_board = 1 }
  :: (son_2_on_board == 0 && son_2 == boat && !on_water)   -> atomic { printf("son_2 get on board\n");  son_2_on_board = 1 }
  
  :: (father_on_board == 1 && !on_water) -> atomic { printf("father goes ashore\n"); father = boat; father_on_board = 0 }
  :: (son_1_on_board == 1 && !on_water)  -> atomic { printf("son_1 goes ashore\n");  son_1 = boat;   son_1_on_board = 0 }
  :: (son_2_on_board == 1 && !on_water)  -> atomic { printf("son_2 goes ashore\n");  son_2 = boat;   son_2_on_board = 0 }
  
  :: (father_on_board || son_1_on_board || son_2_on_board) -> atomic { printf("on_water\n"); on_water = 1 } 
  :: (on_water) -> atomic { printf("arrival\n");  on_water = 0;   boat = 1 - boat }
  od
}

ltl {
  !(safe U (father && son_1 && son_2 && boat))
}