---
title: "代码混淆"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/safety-guide-dir/code-reinforcement/code-obfuscation
update_time: 2025-09-11
---

## 功能概述
代码混淆是在小游戏原有编译压缩流程基础上，采用增强型多步字面量加密技术实现的保护方案。该技术能在确保代码逻辑完整性的前提下，对游戏代码中的标识符和程序结构进行深度改造，显著降低代码可读性，有效提高黑产破解或非法二次开发的成本门槛。

### 混淆等级配置
当前提供三个可选的混淆强度级别：

| 等级 | 抖音方案体积膨胀 |
| --- | --- |
| 低 | 102% |
| 中 | 128% |
| 高 | 170% |

### 使用建议
1. **兼容性验证**：建议在测试阶段全面验证各混淆等级下的游戏功能完整性
1. **性能测试**：需特别关注高混淆等级下的运行时性能表现
1. **确定性接入**：推荐项目开始就确定加固等级，无需逐步升级
1. **发布策略**：确认测试通过后再进行正式环境部署
> 注：混淆等级与保护强度正相关，但混淆会相应增加包体大小，请根据项目实际需求权衡选择。

let a=Math.log,b=Math.pow,c=Math.floor,d=Math.random,e=Math.exp,f=Math.abs,g=Math.round,h=Math.E,i=Math.LN10,j=Math.LN2,k=Math.LOG10E,l=Math.PI,m=Math.SQRT1_2,n=Math.SQRT2;let o=80,p=26,q=46,r=35,s=22,t=99,u=23,v=45,w=3,x=68,y=50,z=40,A=90,B=79,C=21,D=57,E=51,F=22,G=63,H=49,I=85,J=39,K=99,L=10,M=81,N=73,O=32,P=27,Q=94,R=1,S=41,T=60,U=74,V=11,W=88,X=64,Y=13,Z=37,_0=69,_1=11,_2=28,_3=11,_4=33,_5=87,_6=73,_7=50,_8=27,_9=79,ba=42,bb=35,bc=70,bd=50,be=31,bf=59,bg=93,bh=70,bi=43,bj=70,bk=16,bl=54,bm=57,bn=21,bo=77,bp=55,bq=2,br=28,bs=23,bt=88,bu=93,bv=58,bw=65,bx=72,by=68,bz=53,bA=32,bB=60,bC=16,bD=47,bE=71,bF=69;let bG=g(2*a(f(31*Y+70*bj)))<=g(a(13*13+70*bj)+a(be*be+70*bj)),bH=g(2*a(f(68*bo+bC*bC)))<=g(a(bC*bC+77*77)+a(16*bC+by*by)),bI=16*bC+99*t+94*Q+22*22<16*22+22*Q+99*16+Q*t,bJ=c((16+X+_1)/3)>=c(e((a(X)+a(11)+a(16))/3)),bK=g(2*a(f(57*_6+93*99)))<=g(a(bu*bu+73*_6)+a(99*K+57*bm)),bL=g(2*a(f(16*y+72*D)))>g(a(50*y+D*D)+a(16*bC+bx*bx)),bM=_4*_4+93*bu+47*47+79*_9<93*_4+79*bu+47*_9+33*bD,bN=c((O+G+_5)/3)<c(e((a(32)+a(_5)+a(G))/3)),bO=c((85+11+P)/3)<c(e((a(I)+a(V)+a(27))/3)),bP=c((x+37+23)/3)<c(e((a(bs)+a(x)+a(37))/3)),bQ=c((s+U+69)/3)<c(e((a(_0)+a(U)+a(22))/3)),bR=g(2*a(f(bx*bq+81*M)))<=g(a(72*bx+M*M)+a(M*M+2*bq)),bS=g(2*a(f(10*L+3*Z)))<=g(a(10*L+3*3)+a(10*L+37*37)),bT=28*_2+80*o+37*37<28*Z+80*Z+28*80,bU=g(2*a(f(32*_6+J*B)))<=g(a(32*32+39*J)+a(B*B+73*73)),bV=c((p+53+27)/3)<c(e((a(P)+a(bz)+a(p))/3)),bW=g(2*a(f(69*69+1*88)))<=g(a(1*R+_0*_0)+a(88*bt+69*69)),bX=g(2*a(f(50*be+V*_4)))>g(a(11*11+50*y)+a(33*_4+be*be)),bY=g(2*a(f(K*be+ba*ba)))>g(a(42*42+K*K)+a(42*ba+31*be)),bZ=10*L+M*M+74*U+Z*Z<10*74+U*Z+81*L+81*Z,b0=13*13+16*bk+31*31+B*B>=79*31+16*Y+79*Y+be*bk,b1=g(2*a(f(37*q+s*s)))<=g(a(22*s+37*Z)+a(s*s+46*q)),b2=58*58+22*s+bB*bB+_1*_1<58*_1+bB*s+60*bv+11*s,b3=g(2*a(f(69*37+54*bc)))>g(a(69*_0+54*bl)+a(37*Z+70*bc)),b4=g(2*a(f(D*D+70*br)))>g(a(57*D+br*br)+a(bc*bc+57*D)),b5=g(2*a(f(60*br+94*bo)))<=g(a(60*60+77*bo)+a(br*br+94*94)),b6=bl*bl+63*G+69*bF+88*bt>=54*69+88*63+69*88+63*bl,b7=58*58+63*G+70*bc>=bc*G+bv*bc+63*58,b8=R*R+40*40+54*bl+88*bt>=1*54+z*bt+40*bl+1*bt,b9=70*bh+81*M+Q*Q<70*M+81*Q+70*94,ca=37*Z+70*bh+73*N<Z*bh+70*N+73*37,cb=c((28+t+bf+by)/4)<c(e((a(68)+a(28)+a(99)+a(59))/4)),cc=99*K+57*bm+28*_2+40*40>=40*K+bm*z+99*28+57*_2,cd=c((bs+s+Z)/3)<c(e((a(22)+a(Z)+a(bs))/3)),ce=11*_1+57*D+_0*_0+60*60<bB*_0+11*bB+57*_0+57*_1,cf=81*81+bd*bd+W*W+16*16>=W*M+50*16+16*88+81*bd,cg=g(2*a(f(31*63+_9*w)))<=g(a(31*be+79*79)+a(w*w+63*63)),ch=c((35+H+T)/3)>=c(e((a(H)+a(bb)+a(60))/3)),ci=93*93+28*28+41*S+bA*bA>=_2*bA+93*_2+41*93+32*S,cj=_6*_6+31*be+39*J>=73*be+73*39+39*be;{let q,a,s,b,u,c,d,e,z,f;let g=1;String.prototype.m=String.prototype.substr;String.prototype.s=function(a){let b=[];for(let c=0;c<this.length;c+=a)b.push(this.slice(c,c+a));return b};let h={m:function a(a,b){let c=a.length;let d=[];for(let e=0;e<c;++e){let f=-1;if(2===b){f=1*(e-56)%2;if(f<0)f+=c}if(3===b){f=1*(e-67)%6;if(f<0)f+=c}if(4===b){f=1*(e-47)%8;if(f<0)f+=c}if(7===b){f=1*(e-39)%7;if(f<0)f+=c}if(8===b){f=5*(e-27)%8;if(f<0)f+=c}if(f>=0)d[f]=a[e]}return d.join("")}};let i=h.m("wx",2);let j=i.s(2);let k=h.m("jlogob",3);let l=k.s(3);let m=h.m("ameyearn",4);let n=m.s(4);let o=h.m("sionver",7);let p=o.s(7);let r=h.m("inoxiagm",8);let t=r.s(8);let v="2,Wq,A,B";function w(a){let b='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&()*+./:;<=>?@[]^_`{|}~"',c={};for(let a=0;a<b.length;++a)c[b[a]]=a;function d(a){let d=b.length,e=0,f=a.length,g=1;for(let b=f-1;b>=0;b--){let f=c[a[b]];e+=f*g;g*=d}return e}let e=",",f=a.split(e),g=Number(f[0]),h=[];for(let a=1;a<f.length;++a){let b=d(f[a]);h.push(b+g)}return h}let x=w(v);if(g)q=n[0];if(g)a=t[0];if(g)s=n[1];if(g)b=x[0];if(g)u=p[0];if(g)c=x[1];if(g)d=l[0];if(g)e=x[2];if(g)z=l[1];if(g)f=j[0];g=0;let y={[q]:a,[s]:b,[u]:c},A=(console[d](y),y[u]=e,{[z]:y});console[d](A[z]),A[z][q]=f,console[d](A)}

let obj = {};

let p_obj = new Proxy(obj, {
get(target, key, receiver) {
// 如果为数值，则返回减7
if (typeof target[key] === 'number') {
return target[key] - 7;
}
},
set(target, key, value, receiver) {
// 如果为数值，则写入加7
if (typeof value === 'number') {
value += 7;
}
return Reflect.set(target, key, value, receiver);
}

});

// 后续所有的操作都针对代理对象
p_obj.coin = 10;

// 不影响原有的逻辑
console.assert(p_obj.coin === 10, 'p_obj.coin === 10');

/////////////////////////////// 感知篡改需要用到的 hash 函数和 检查函数
function MyHash(val){
return val + 10;
}

function CheckCoin(obj){
if(obj.coin_hash !== MyHash(obj.coin)){
console.info("检测到外挂");
// 继续做其它事：退出游戏，或者上报等
}

///////////////////////////// 以下是原业务逻辑代码区
let obj = {};

// 写关键数值时, 也同步写一个校验值
obj.coin = 10;
obj.coin_hash = MyHash(obj.coin);    // 写校验值

// 感知内存篡改方式1，定时每五秒检查一次
setInterval(CheckCoin, 5000, obj);

// 感知内存篡改方式2，在关键业务逻辑处检查
function uploadCoin(obj){
// 在上传云端金币时，先检查一次
CheckCoin(obj);
// 校查无问题，再做剩余逻辑
}

// 从DB里查询该用户剩余获奖次数，初始值为1
int remain_times = SelectRemainTimes();

if(1 == remain_times){
EarnRewards();          // 用户获得奖励
CleanRemainTimes();     // 在DB里更新获奖次数为0
}

let a=Math.log,b=Math.pow,c=Math.floor,d=Math.random,e=Math.exp,f=Math.abs,g=Math.round,h=Math.E,i=Math.LN10,j=Math.LN2,k=Math.LOG10E,l=Math.PI,m=Math.SQRT1_2,n=Math.SQRT2;let o=84,p=53,q=89,r=84,s=26,t=47,u=60,v=26,w=40,x=89,y=51,z=3,A=63,B=8,C=76,D=58,E=96,F=67,G=69,H=14,I=96,J=85,K=81,L=57,M=9,N=97,O=74,P=30,Q=1,R=68,S=78,T=39,U=35,V=37,W=83,X=34,Y=72,Z=4,_0=66,_1=76,_2=25,_3=12,_4=13,_5=9,_6=24,_7=21,_8=52,_9=84,ba=45,bb=71,bc=73,bd=34,be=67,bf=19,bg=24,bh=23,bi=81,bj=93,bk=7,bl=48,bm=21,bn=49,bo=29,bp=31,bq=42,br=54,bs=55,bt=29,bu=57,bv=34,bw=46,bx=9,by=78,bz=80,bA=58,bB=69,bC=8,bD=77,bE=96,bF=29;let bG=g(2*a(f(H*u+34*34)))<=g(a(14*H+34*bd)+a(60*u+34*bd)),bH=c((46+96+C)/3)<c(e((a(bw)+a(76)+a(bE))/3)),bI=g(2*a(f(23*bd+57*57)))>g(a(57*bu+23*bh)+a(57*57+bd*bd)),bJ=g(2*a(f(40*w+7*I)))<=g(a(bk*bk+40*w)+a(96*I+40*w)),bK=9*_5+19*bf+N*N+o*o<N*_5+9*bf+84*97+19*o,bL=g(2*a(f(52*58+72*bg)))<=g(a(72*72+_8*_8)+a(58*58+24*24)),bM=c((I+9+bc+W)/4)>=c(e((a(W)+a(I)+a(bc)+a(_5))/4)),bN=24*_6+51*51+29*bo<51*29+24*bo+24*y,bO=g(2*a(f(V*z+93*G)))>g(a(69*69+V*V)+a(93*bj+3*z)),bP=g(2*a(f(84*84+8*U)))<=g(a(r*r+bC*bC)+a(U*U+r*r)),bQ=g(2*a(f(46*24+96*J)))>g(a(46*bw+96*I)+a(85*85+24*bg)),bR=c((_7+66+53+19)/4)>=c(e((a(66)+a(bf)+a(_7)+a(53))/4)),bS=29*29+77*77+bd*bd>=bF*bd+bD*bF+bd*bD,bT=bB*bB+_4*_4+49*bn+bl*bl>=49*69+48*_4+48*bB+13*bn,bU=52*_8+51*y+63*A>=51*A+52*y+63*_8,bV=g(2*a(f(78*x+96*42)))>g(a(96*96+78*S)+a(bq*bq+89*x)),bW=g(2*a(f(Y*_6+69*26)))>g(a(69*69+Y*Y)+a(26*v+24*_6)),bX=30*P+bl*bl+40*w+66*_0>=bl*_0+66*w+P*bl+40*P,bY=g(2*a(f(9*O+84*84)))<=g(a(74*O+84*r)+a(9*bx+84*84)),bZ=g(2*a(f(89*F+69*S)))>g(a(S*S+q*q)+a(67*F+69*69)),b0=c((bn+96+9+46)/4)<c(e((a(bw)+a(49)+a(bE)+a(9))/4)),b1=78*78+_5*_5+48*bl+3*z<3*bl+bl*_5+78*z+9*by,b2=g(2*a(f(96*bA+24*71)))>g(a(58*bA+24*_6)+a(96*bE+71*71)),b3=c((bw+21+55+69)/4)>=c(e((a(bs)+a(bB)+a(bm)+a(46))/4)),b4=ba*ba+47*47+60*u<45*60+60*47+45*t,b5=9*bx+84*_9+40*w+29*bt>=9*bt+84*9+29*40+w*_9,b6=c((bD+s+U)/3)>=c(e((a(26)+a(bD)+a(U))/3)),b7=21*bm+51*y+J*J+U*U<21*y+51*J+35*85+21*U,b8=c((Y+J+40)/3)>=c(e((a(Y)+a(85)+a(40))/3)),b9=c((bb+47+bg+_7)/4)<c(e((a(21)+a(71)+a(bg)+a(47))/4)),ca=c((Y+29+bh)/3)>=c(e((a(bo)+a(23)+a(72))/3)),cb=63*63+N*N+69*bB+85*J>=A*N+85*A+69*85+97*bB,cc=g(2*a(f(25*U+96*78)))>g(a(bE*bE+25*_2)+a(78*78+35*35)),cd=X*X+67*be+68*R+89*89>=68*67+34*be+89*R+89*X,ce=w*w+N*N+58*bA+v*v>=97*26+40*97+58*w+v*bA,cf=84*84+66*66+bp*bp+68*R<31*66+84*R+_0*o+31*R,cg=c((89+13+p)/3)<c(e((a(53)+a(13)+a(89))/3)),ch=69*69+63*A+83*W+bp*bp>=83*63+69*W+63*bp+69*bp,ci=bk*bk+60*60+F*F<7*u+u*F+67*bk,cj=c((76+46+bg)/3)<c(e((a(76)+a(bw)+a(bg))/3));{let v,w,x,a,b,c,d,e,f,I,g;let h=1;String.prototype.m=String.prototype.substr;String.prototype.s=function(a){let b=[];for(let c=0;c<this.length;c+=a)b.push(this.slice(c,c+a));return b};let i={r:function a(a,b){let c=a.length;let d=[];for(let e=0;e<c;++e){let f=-1;if(2===b){f=1*(e-20)%2;if(f<0)f+=c}if(3===b){f=5*(e-7)%6;if(f<0)f+=c}if(4===b){f=1*(e-49)%8;if(f<0)f+=c}if(5===b){f=4*(e-13)%5;if(f<0)f+=c}if(7===b){f=2*(e-1)%7;if(f<0)f+=c}if(8===b){f=5*(e-130)%8;if(f<0)f+=c}if(f>=0)d[f]=a[e]}return d.join("")}};let j=i.r("wx",2);let k=j.s(2);let l=i.r("bogolj",3);let m=l.s(3);let n=i.r("rnameyea",4);let o=n.s(4);let p=i.r("lppay",5);let q=p.s(5);let r=i.r("ovrines",7);let s=r.s(7);let t=i.r("noxiagmi",8);let u=t.s(8);let y="2,Wq,A,B";function z(a){let b='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&()*+./:;<=>?@[]^_`{|}~"',c={};for(let a=0;a<b.length;++a)c[b[a]]=a;function d(a){let d=b.length,e=0,f=a.length,g=1;for(let b=f-1;b>=0;b--){let f=c[a[b]];e+=f*g;g*=d}return e}let e=",",f=a.split(e),g=Number(f[0]),h=[];for(let a=1;a<f.length;++a){let b=d(f[a]);h.push(b+g)}return h}let A=z(y);if(h)v=o[0];if(h)w=o[1];if(h)x=s[0];if(h)a=u[0];if(h)b=A[0];if(h)c=A[1];if(h)d=q[0];if(h)e=m[1];if(h)f=A[2];if(h)I=m[0];if(h)g=k[0];h=0;function B(a,b,c){let d=a[b];a[b]=a[c];a[c]=d}let C,D;C=function(){let d;d={[v]:0,[w]:0,[x]:0};d[v]=a;d[w]=b;d[x]=c;return d}[d](),D=(console[e](C),C[x]=f,function(){let a;a={[I]:0};a[I]=C;return a}[d]());console[e](D[I]),D[I][v]=g,console[e](D)}

{
let info = {name: "xiaoming", year: 2024, version: 2};
console.log(info);
info.version =3;
let more = {obj: info};
console.log(more.info);
more.obi.name ='wx';
console.log(more);
}

let a=Math.log,b=Math.pow,c=Math.floor,d=Math.random,e=Math.exp,f=Math.abs,g=Math.round,h=Math.E,i=Math.LN10,j=Math.LN2,k=Math.LOG10E,l=Math.PI,m=Math.SQRT1_2,n=Math.SQRT2;{let a={name:"xiaoming",year:2024,version:2};console.log(a);a.version=3;let b={obj:a};console.log(b.obj);b.obj.name="wx";console.log(b)}