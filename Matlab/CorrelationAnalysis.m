% Analysis of input data. TODO descirbe this file
%% Read data
file = "C:\Users\Jesper\Documents\MATLAB\Ex-jobb\Allt utom golf_se.xlsx";
%file = "C:\Users\fredr\Google Drive\Universitetet_i_halmstad\Examensarbete_C3\Rapporter\data\Allt utom golf_se.xlsx";
%file = "D:\Google drive\Universitetet_i_halmstad\Examensarbete_C3\Rapporter\data\Allt utom golf_se.xlsx";
%file = "C:\Users\fredr\Google Drive\Universitetet_i_halmstad\Examensarbete_C3\Rapporter\data\golf_se.csv"

data = readtable(file);
dataLen = length(data.Comment);
NPS = data.NPS;
comment = data.Comment;

%% Data masking
mask = ~isnan(NPS);
NPS = NPS(mask);
comment = comment(mask);

%% Data processing
setLen = length(NPS);
% Cleaning: remove & record... stuff
[caps,punctuation] = deal(zeros(setLen,1));
for i = 1:setLen
    caps(i) = sum(isstrprop(comment{i}, 'upper'));
    punctuation(i) = sum(isstrprop(comment{i}, 'punct'));
    comment{i} = comment{i}(~isstrprop(comment{i}, 'punct'));
end
comment = lower(comment);

% B�g of words
splitComment = regexp(comment, ' ', 'split');
words = horzcat(splitComment{:});
[uniqueorn,iw,cw] = unique(words);
[freq, idx] = histcounts(cw,1:max(cw)+1);
[~,index] = sort(freq,'descend');
% uniqueorn(idx(index(1:100)))'

% Help function to auto padd inputs to corr
paddedCorr = @(pattern,comment) corr([double(pattern)-mean(pattern) zeros(1,max(length(comment)-length(pattern),0))]'...
    ,[double(comment)-mean(comment) zeros(1,max(length(pattern)-length(comment),0))]');

% Main loop
warning('off','MATLAB:polyfit:PolyNotUnique'); % since some comments are blank
[corrOch, corrBra ,emoji, lengthOfComment, avrg] = deal(zeros(setLen,1));
polly = zeros(setLen,2);
chars = cell(setLen,1);
for i = 1:setLen
    chars{i} = int16(comment{i});
    lengthOfComment(i) = length(chars{i});
%    polly(i,1:2) = polyfit(1:length(chars{i}),double(chars{i}),min(1,length(chars{i})));
%     emoji(i) = sum(isstrprop(comment{i}, 'graphic')); 
%     punctuation(i) = sum(isstrprop(comment{i}, 'punct'));
    corrOch(i) = paddedCorr('och',comment{i});
    corrBra(i) = paddedCorr('bra',comment{i});
    avrg = mean(comment{i});
end

% [corrMen] = deal(zeros(setLen,1));
% for i = 1:setLen
%     corrMen(i) = paddedCorr('men',comment{i});
% end

corrOch(isnan(corrOch)) = 0;
corrBra(isnan(corrBra)) = 0;
% xcov(double('ass')',double('assassin')') % ad hoc filter exempel

%% Data presentation
disp(corr([NPS,lengthOfComment]))

%% Graveyard
% cumulativeFreq = zeros(100,1)
% for i = 1:100 cumulativeFreq(i) = sum(freq>=i); end
% plot(cumulativeFreq)

