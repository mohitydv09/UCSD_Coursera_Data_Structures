# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            #add to stack
            b=Bracket(next,i)
            opening_brackets_stack.append(b)
            # print(opening_brackets_stack)
            continue

        if next in ")]}":
            # Process closing bracket, write your code here
            #agar last aur ye same nahi he to kahtam 
            if opening_brackets_stack and are_matching(opening_brackets_stack[-1].char,next):
                opening_brackets_stack.pop()
                # print('removed last racket:',opening_brackets_stack)
            else:
                return i+1
        
    if len(opening_brackets_stack)==0:
        return "Success"
    else:
        return (opening_brackets_stack[-1].position) +1

def main():
    text = input()
    # text="[]"
    # text="{y9{q(([!j[(T{a[CZ[[M[({ZAA[6([g(B]{(3(9{J8y{[x(n(ur(H{J[{(g[e{LPFM(K[!9([iq[:[0L(XX{p{;[(s{O[{[{{({:N]b{[:{({w2(7({K{{{Y{(({{(U0XKr{jz[[q4W(v(((S{EE(([J[lUSi({[9atHv[Avt{.(7{4z[qc{({{(,[gEE({9{O(s[(([[!(n{SUr4[79(x{([(4{L,{y(Pvu{[[4z[(aP{![l[]L]}j)]Mk]]}?)}t}k9J)9]V)u})]}0)]3]EQ)u)H:]E).}}])33])m?F}c})u}]QC}1)}b]:}ZeH)M]]))y?g})C)R4)z)e]]n}D)q}?})EA)}}}}kg}))M})}v]d}}0)H}u}za],}k]}ik)]YT}9}G)]lu].I]6)z])}AA7]G)}Jv]2V}MNq))nv)]6pU3}t};4t))x}8F)Lq]y)]y8}kT)qG]c]bL]]j0}H)]]l))lc}E}{:[(n)E]x3}{{2[Ge?([]2)9T]}}chMq[!l[[1{[F[Bw([PV[j2z(k{Km{{sO{:[V({k[cU(;,W{({(((uV()c.s)))}q)}L)K.]})]F}B}w}iD})B]FC!f]K)]3v]jV}6]]qg{0{z([A{W}])Z}d}{u{{J1}O}M}l{hRr(W{f()}Q)Q4}{c[i{f([(uP[[{![E4d[I[x{a(.(NZ(T{Pul(uy;{}Vi)})4))}VV]d]V]}]Eh]4)y;]v1)}]}s[{N}][H[4T(w(({{[(Q((cjn[7{OtS()J}]))3i)]Z6}?g};u)))]][(j7((z(:(m[{Qd({F[({(C(d(xy{qml[.(?{[;(T{yq((9:(H[I4{{m[oc;(B[Q?[{[{9(GK(l[[(Os[Y(V{E{X(o(D[{[Y[q[vIF((p{[uUt{[kt{.(Re{EYX[{.G{([(((a[{,{In(ZL({9H{q[25{;[[s[[u{bY[(yV(([[{g{Y[zz[V{([eHw(H;{{39U[6q({C[{;(d[(WP(kgYx;{k{lq{LK[(Gm{,[:[!(qKh{(05[(U[r6[3[JZ{f9{c!([(b,{j{(C(3l8[1{wS{X{pW(k[Q{r{7{LQ[({U(k{{b[(k{uE2[Me(SL({pQ(h[!{zF{a[[Z[1M{P{l[s0{(7[(v[({3n([k8({{{(w[[{E(8d[h3(G{[!B[I{t(5n[s[{Tn(!(XmC{({Ig[E(6([[[(5[N[{N{{{P[b(EHn[c[y({M{9K{(K:({[({;(J[m(e4[X{(T(3K{z:{yS{f[7{V7[E{![5[y[{{[[(Q[O!b((W)x)cmt]u)]B]SxuH}p}VP]M]Q]n}]}r]}Z}:n}v)H)XZ}eR]0)6]g)}j)DE]Hb:mQOF}n))Rwy}P!S}7}X4i)V]]Uv)]S}t}J}}g}9HDX],])P]7p]ut])D)]2}o9)}5))}N]]?aA)r}]]u5}1)4o])F}96]]8)F}}o}i)v1]T)}Y)gM])Wi]4)c}E]}p}eAh]oS]5UeQ]tvX}32}4])}Q)aw)]?K}y):47i7]}})E})]Q!e}U:}:TC}d]Gn)6}}t}]y)RA)}z})s])LHR}}kb]e]])cM])t})aU]]}9)t1]xZd}p}A}W))I])zH}W]}KL)Bg]2}H}Y)P2]xX)9}W].H]97}?}Hbz]]))g7Z)dR]}];]]]ha}P]dw}YB}w))}s}]f)x))k]Y)}m}p]az})9}]y}]})aBe)pN]]O]XIA}])y2)}}v)]y)]])ca)}:]y}]3I]n)d]}}])GL))}2)Z]}zw)1]}3QL)B)):WP})b]}H)}xNe]P)33)gM)))4](sK(nZ))rb{3{8[[(0(y!{[l{f{2{(B{7(P[t[a[{{:{!B0k{7[:[g{{F[P[aje({(sp3(?{Njc({H{o(F1K[p{[,[([[p6[[T[S]]]W]]olK)aY]U]RJ}hbt]It)7}}:)5})IY)}V)a]]sr3}td}]]LH?}Qg}V}}cq0]n]HtI]U)r}t)p}c}}Y]}2)1)L].ER]Z}r}"
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
