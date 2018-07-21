// Coursera golang hw1
package main

import (
	"fmt"
	"io"
	"os"
	"path/filepath"
	"sort"
	"strconv"
)

func getFileSize(filepath string) int64 {
	descriptor, err := os.Stat(filepath)
	if err != nil {
		panic(err)
	}
	return descriptor.Size()
}

func isDirectory(path string) (bool, error) {
	fileInfo, err := os.Stat(path)
	return fileInfo.IsDir(), err
}

func getPrefix(isLast bool) string {
	ch := "├"
	if isLast {
		ch = "└"
	}
	return ch + "───"
}

func getLine(path string, prefix string, isLast bool) string {
	filename := filepath.Base(path)
	if isDir, _ := isDirectory(path); !isDir {
		filesize := getFileSize(path)
		if filesize > 0 {
			filename += " (" + strconv.FormatInt(filesize, 10) + "b)"
		} else {
			filename += " (empty)"
		}
	}
	return prefix + getPrefix(isLast) + filename + "\n"
}

func filter(paths []string, predicate func(string) bool ) []string {
	filtered := make([]string, 0)
	for _, path := range paths {
		if predicate(path) {
			filtered = append(filtered, path)
		}
	}
	return filtered
}

func recDirTree(out io.Writer, path string, printFiled bool, depth int, prefix string) error {
	currentItems, err := filepath.Glob(path + "/*")
	if err != nil {
		fmt.Println(err)
	}
	if !printFiled {
		currentItems = filter(currentItems, func(st string) bool {
			isDir, _ := isDirectory(st)
			return isDir
		})
	}
	sort.Strings(currentItems)
	for idx, item := range currentItems {
		isLast := idx == len(currentItems) - 1
		out.Write([]byte(getLine(item, prefix, isLast)))
		if isDir, _ := isDirectory(item); isDir {
			newPrefix := prefix
			if !isLast {
				newPrefix += "│"
			}
			newPrefix += "\t"
			recDirTree(out, item, printFiled, depth + 1, newPrefix)
		}
	}
	return nil
}

func dirTree(out io.Writer, path string, printFiled bool) error {
	return recDirTree(out, path, printFiled, 0, "")
}

func main() {
	out := os.Stdout
	if !(len(os.Args) == 2 || len(os.Args) == 3) {
		panic("usage go run main.go . [-f]")
	}
	path := os.Args[1]
	printFiles := len(os.Args) == 3 && os.Args[2] == "-f"
	err := dirTree(out, path, printFiles)
	if err != nil {
		panic(err.Error())
	}
}
