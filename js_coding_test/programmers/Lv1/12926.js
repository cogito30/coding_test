// 시저 암호
function solution(s, n) {
    var answer = '';
    const capitalAlphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const smallAlphabets = "abcdefghijklmnopqrstuvwxyz";
    for (let i = 0; i < s.length; ++i) {
        if (s[i] >= 'A' && s[i] <= 'Z') {
            answer += capitalAlphabets[parseInt((capitalAlphabets.indexOf(s[i]) + n) % 26)];
        } else if (s[i] >= 'a' && s[i] <= 'z') {
            answer += smallAlphabets[parseInt((smallAlphabets.indexOf(s[i]) + n) % 26)];
            
        } else {
            answer += s[i];
        }
    }
    return answer;
}