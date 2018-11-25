fileid = fopen('download_records4k_v2.txt');
formatSpec = '%f';
A = fscanf(fileid, formatSpec);
ecdf(A, 'Bounds', 'on');