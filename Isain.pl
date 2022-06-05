%A_alan
%B_brenda
%C_carlos
%D_david
%F_fernando
%H_hijinio
%I_isain
%J_jimena
%L_luz
%M_maria


mayor(alan,brenda).
mayor(brenda,carlos).
mayor(carlos,david).
mayor(david,fernando).
mayor(fernando,hijinio).
mayor(hijinio,isain).
mayor(isain,jimena).
mayor(jimena,luz).
mayor(luz,maria).
mayor(maria,todos).

muchomayor(A,C):-mayor(A,B),mayor(B,C).
muchomayor(D,H):-mayor(D,F),mayor(F,H).
muchomayor(I,L):-mayor(I,J),mayor(J,L).
muchomayor(J,M):-mayor(J,L),mayor(L,M).
muchomayor(B,D):-mayor(B,C),mayor(C,D).
muchomayor(C,F):-mayor(C,D),mayor(D,F).
muchomayor(F,I):-mayor(F,H),mayor(H,I).
muchomayor(H,J):-mayor(H,I),mayor(I,J).