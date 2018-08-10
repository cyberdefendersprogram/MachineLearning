import csv
import os
dic = {"dhcp.log":["ts", "uid", "id.orig_h", "id.orig_p", "id.resp_h", "id.resp_p", "mac", "assigned_ip", "lease_time", "trans_id"], "dns.log":["ts", "uid", "id.orig_h", "id.orig_p", "id.resp_h", "id.resp_p", "proto", "port", "query", "qclass", "qclass_name", "qtype", "qtype_name", "rcode",	"rcode_name", "QR",	"AA", "TC",	"RD", "Z", "answers", "TTLs", "rejected"], "ftp.log":["ts", "uid", "id.orig_h", "id.orig_p", "id.resp_h", "id.resp_p", "user", "password", "command", "arg","mime_type", "file_size", "reply_code", "reply_msg", "passive", "orig_h", "resp_h", "resp_p", "fuid"], "ssh.log":["ts", "uid", "id.orig_h", "id.orig_p", "id.resp_h", "id.resp_p", "status", "direction", "client", "server", "resp_size"], "files.log":["ts", "fuid", "tx_hosts", "rx_hosts", "conn_uids", "source", "depth", "analyzers", "mime_type", "filename",	"duration", "local_orig", "is_orig", "seen_bytes", "total_bytes", "missing_bytes", "overflow_bytes", "timedout","parent_fuid", "md5/sha1/sha256", "extracted"], "http.log":["ts", "uid", "id.orig_h", "id.orig_p", "id.resp_h",	"id.resp_p", "trans_depth",	"method", "host", "uri", "referrer", "user_agent",	"request_ body_len", "response_ body_len",	"status_code",	"status_msg", "info_code", "info_msg", "filename",	"tags",	"username",	"password",	"proxied",	"orig_fuids",	"orig_mime_types",	"resp_fuids",	"resp_mime_types"], "notice.log":["ts",	"uid",	"id.orig_h",	"id.orig_p", "id.resp_h", "id.resp_p", "fuid", "file_mime_type", "file_desc",	"proto", "note",	"msg",	"sub",	"src",	"dst",	"p", "n",	"peer_descr",	"actions",	"suppress_for",	"dropped"],"smtp.log":["ts", "uid",	"id.orig_h",	"id.orig_p",	"id.resp_h",	"id.resp_p",	"proto",	"trans_depth",	"helo",	"mailfrom",	"rcptto",	"date",	"from",	"to",	"in_reply_to",	"subject",	"x_originating_ip",	"first_received",	"second_received",	"last_reply",	"path",	"user_agent",	"tls",	"fuids", "is_webmail"],"ssl.log":["ts",	"uid",	"id.orig_h",	"id.orig_p",	"id.resp_h",	"id.resp_p", "version",	"cipher",	"server_name",	"session_id",	"subject",	"issuer_subject",	"not_valid_before",	"not_valid_after",	"last_alert",	"client_subject",	"clnt_issuer_subject",	"cer_hash",	"validation_status"],"tunnel.log":["ts",	"uid",	"id.orig_h",	"id.orig_p",	"id.resp_h",	"id.resp_p",	"tunnel_type",	"action"],"weird.log":["ts",	"uid", "id.orig_h",	"id.orig_p",	"id.resp_h",	"id.resp_p",	"name",	"addl",	"notice",	"peer"]}

path = "network"
for filename in os.listdir(path):
	with open(path+"/"+filename.replace("log","csv"), 'w+', encoding='utf-8', newline='') as csvfile:
		w = csv.writer(csvfile, dialect='excel')
		with open(path+"/"+filename, encoding="utf8") as file:
			lines = file.read().split('\n')
			lines=lines[:-1]
	        # print(lines)
			files = [dic[filename]]
		for line in lines:
				cells = []
				for item in line.split('\t'):
					if item=="-":
						cells.append(item.replace("-",""))
					else:
						cells.append(item)
				files.append(cells)
		w.writerows(files)